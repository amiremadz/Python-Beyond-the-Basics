import os

class ConfigKeyError(Exception):
    
    def __init__(self, config_dict, key):
        self.key = key
        self.available_keys = config_dict.keys()    

    def __str__(self):
        return 'key {0} not found. Available keys: ({1})'.format(self.key, ', '.join(self.available_keys))

class ConfigDict(dict):
    
    def __init__(self, file_path):

    	self._file_path = file_path

        if not os.path.isfile(self._file_path):
            try:
                open(self._file_path, 'w').close()
            except IOError:
                raise IOError("File path not valid")

        with open(self._file_path) as file:
            for line in file:
                key, val = line.split('=', 1)
                super(ConfigDict, self).__setitem__(key, val)

    def __setitem__(self, key, val):
    	super(ConfigDict, self).__setitem__(key, val)
    	
    	with open(self._file_path, 'a+') as file:
    	   	file.write('{0}={1}\n'.format(key, val))

    def __getitem__(self, key):
        try:
            return super(ConfigDict, self).__getitem__(key)
        except KeyError:
            raise ConfigKeyError(self, key)        


