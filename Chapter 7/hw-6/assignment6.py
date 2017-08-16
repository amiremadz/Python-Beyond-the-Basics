import os.path

class ConfigKeyError(Exception):
	def __init__(self, config_dict, key):
		self._keys = config_dict.keys()
		self._key = key

	def __str__(self):	
		return "key {0} does not exist. available keys are ({1}).".format(self._key, ', '.join(self._keys))

class ConfigDict(dict):
	
	def __init__(self, filename):
		self._filename = filename

		if not os.path.isfile(self._filename):
			try:
				open(self._filename, 'w').close()
			except IOError:
				raise IOError("path does not exist.")	
		else:
			with open(self._filename, 'r') as fh:
				for line in fh:
					line = line.rstrip()
					key, val = line.split('=', 1)
					super(ConfigDict, self).__setitem__(key, val)

	def __getitem__(self, key):
		try:
			return super(ConfigDict, self).__getitem__(key)
		except KeyError:
			raise ConfigKeyError(self, key)	
	
	def __setitem__(self, key, val):	
		super(ConfigDict, self).__setitem__(key, val)
		
		if 0:
			with open(self._filename, 'a+') as fh:
				fh.write('{0}={1}\n'.format(key, val))
		else:
			with open(self._filename, 'w+') as fh:
				for key, val in self.items():
					fh.write('{0}={1}\n'.format(key, val))
