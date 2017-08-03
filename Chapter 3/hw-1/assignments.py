
# class MaxSizeList(object):

# 	def __init__(self, max):
# 		self.max = max
# 		self.list = []
# 		self.length = 0

# 	def push(self, val):
# 		if(self.length >= self.max):
# 			self.list.pop(0)
# 			self.length -= 1
		
# 		self.list.append(val)
# 		self.length += 1
		
# 	def get_list(self):	
# 		return self.list

# 	def get_length(self):
# 		return self.length

class MaxSizeList(object):

	def __init__(self, max):
		self.max = max
		self.list = []
		
	def push(self, val):
		if(len(self.list) >= self.max):
			self.list.pop(0)
			
		self.list.append(val)
		
	def get_list(self):	
		return self.list

	def get_length(self):
		return len(self.list)
