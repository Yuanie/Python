def product(*args):
	if (len(args) == 0):
		raise TypeError
	else:
		s = 1
		for i in args:
			if not isinstance(i,(int, float)):
				raise TypeError
			s *= i
		print(s)

		
product(2)
product(3,4,2)
product(1,2,3,4,5)
