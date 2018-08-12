from functools import reduce 
digits = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, \
		'6' : 6,  '7' : 7, '8' : 8, '9' : 9}
		
		
def str2int(s):
	def chr2num(s):
		return digits[s]
		
	return reduce(lambda x, y: 10 * x + y, map(chr2num, s))
	
S = input("Input your string:")
print(str2int(S))
print(type(str2int(S)))