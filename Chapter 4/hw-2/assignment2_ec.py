import abc
import csv
import datetime

class WriteFile(object):
	__metaclass__ = abc.ABCMeta

	def __init__(self, name):
		dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
		self.name = dt_str+'_'+name
		self.file = None

	@abc.abstractmethod
	def write(self, str):
		return

	@abc.abstractmethod
	def close():
		return 

class LogFile(WriteFile):
	def __init__(self, name):
		super(LogFile, self).__init__(name)
		self.file = open(self.name, "wb")
		
	def write(self, str):
		self.file.write(str+'\n')

	def close(self):
		self.file.close()	

class DelimFile(WriteFile):
	def __init__(self, name):
		super(DelimFile, self).__init__(name)
		self.file = open(self.name, 'wb')

	def write(self, list):
		wr = csv.writer(self.file, delimiter=',')
		wr.writerow(list)

	def close(self):
		return
