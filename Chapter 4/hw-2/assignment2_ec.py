import abc
import datetime

class WriteFile(object):
	__metaclass__ = abc.ABCMeta

	def __init__(self, file_name):
		self.file_name = file_name
		self.file = open(self.file_name, 'wb')

	@abc.abstractmethod
	def write(self, this_line):
		return

	def close(self):
		self.file.close()

	def write_line(self, this_line):
		self.file.write(this_line + '\n')
		
class LogFile(WriteFile):
	def write(self, this_line):
		dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
		self.write_line('{0}	{1}'.format(dt_str, this_line))	
	
class DelimFile(WriteFile):
	def __init__(self, name, delim):
		super(DelimFile, self).__init__(name)
		self.delim = delim

	def write(self, list):
		this_line = self.delim.join(list)
		self.write_line(this_line)