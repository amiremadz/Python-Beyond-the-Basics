import datetime

class WriteFile(object):

	def __init__(self, file_name, Formatter):
		self.file = open(file_name, 'w')
		self.formatter = Formatter()
		
	def write(self, data):
		self.file.write(self.formatter.format(data))
		self.file.write('\n')

	def close(self):	
		self.file.close()
		
class CSVFormatter(object):
	def __init__(self, delim = ','):
		self.delim = delim

	def format(self, list):

		# for indx, item in enumerate(list):
		# 	if self.delim in item:
		# 		list[indx] = '\"' + item + '\"'

		def helper(x):
			if self.delim in x:
				return '\"' + x + '\"'
			return x			

		list = map(helper, list)		

		txt = self.delim.join(list)
		return txt

class LogFormatter(object):

	def format(self, txt):
		dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
		return '{0}		{1}'.format(dt_str, txt)