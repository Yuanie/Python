def creatCounter():
	i = 0
	def counter():
		nonlocal i
		i += 1
		return i
	return counter 

counterA = creatCounter()
print(counterA())
print(counterA())
print(counterA())