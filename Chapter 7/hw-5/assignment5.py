import os
import pickle

class InvalidFileError(Exception):

    def __init__(self, extension):
        self.extension = extension

    def __str__(self):
        return '{0} is not a valid file extension!'.format(self.extension)    

class ConfigKeyError(Exception):
    
    def __init__(self, config_key, key):
        self.all_keys = config_key.keys()
        self.key = key
    
    def __str__(self):
        return "key {0} not found. Available keys: ({1})".format(self.key, ', '.join(self.all_keys))

class ConfigDict(dict):
    
    config_dir = './configs'

    def __init__(self, name):
        self._filepath = os.path.join(ConfigDict.config_dir, name)
        self._fileextension = name.split('.')[1]

        if not os.path.isfile(self._filepath):
            try:
                if self._fileextension == 'txt':
                    open(self._filepath, 'w').close()
                elif self._fileextension == 'pickle':
                    with open(self._filepath, 'w') as fh:
                        pickle.dump(self, fh)
                else:
                    raise InvalidFileError(self._fileextension)
            except IOError:
                raise IOError('path does not exist!')                    

        with open(self._filepath) as fh:
            if self._fileextension == 'txt':
                for line in fh:
                    key, val = line.split('=', 1)
                    super(ConfigDict, self).__setitem__(key, val)
            elif self._fileextension == 'pickle':
                unpickled_dict = pickle.load(fh)
                self.update(unpickled_dict)
            else:
                raise InvalidFileError(self._fileextension)   

    def __getitem__(self, key):
        if not key in self.keys():
            raise ConfigKeyError(self, key)
        return super(ConfigDict, self).__getitem__(key)


    def __setitem__(self, key, val):  

        if self._fileextension == 'txt':
            # Method 1 for writing to a text config file.
            super(ConfigDict, self).__setitem__(key, val)
            with open(self._filepath, 'w') as fh:
                for key, val in self.items():
                    fh.write('{0}={1}\n'.format(key, val))

            # Method 2 for writing to a text config file
            #with open(self._filepath, 'a') as fh:
            #    fh.write('{0}={1}\n'.format(key, val))
            #super(ConfigDict, self).__setitem__(key, val)
        elif self._fileextension == 'pickle':
            # Writing to a pickle file
            super(ConfigDict, self).__setitem__(key, val)
            with open(self._filepath, 'w') as fh:
                pickle.dump(self, fh)
        else:
            raise InvalidFileError(self.fileextension)



