
class ConfigDict(dict):
    
    def __init__(self, file_name):

    	self._file_name = file_name

    	try:
    		with open(self._file_name) as file:
    			for line in file:
    				key, val = line.split('=', 1)
    				super(ConfigDict, self).__setitem__(key, val)

    	except:
    		print 'There is no config file.'
    		print 'Creating one.'
    		file = open(self._file_name, 'w+')
	    	file.close()

    def __setitem__(self, key, val):
    	super(ConfigDict, self).__setitem__(key, val)
    	
    	with open(self._file_name, 'a+') as file:
    	   	file.write('{0}={1}\n'.format(key, val))