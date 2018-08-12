class Student(object):
	
	def __init__(self, name, score):
		self.__name = name			#__ : private variable
		self.__score = score 		#__ xxx __ : special variable是可以直接访问的
		
	def get_name(self):
		return self.__name
		
	def get_score(self):
		return self.__score
		
	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))
		
	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')

bart = Student('Simpson', 59)
bart.__name  		#can't call from outside