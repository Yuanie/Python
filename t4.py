from functools import reduce
#convert the string to float type(method 1)
'''
digits = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, \
		'6' : 6,  '7' : 7, '8' : 8, '9' : 9}

def str2num(s):
	return digits[s]
	
def str2float(s):
	List = s.split('.')
	pow = len(List[1])
	List = list(map(str2num, List[0])) + list(map(str2num, List[1]))
	return reduce(lambda x,y : 10 * x + y, List) / (10 ** pow)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')	
'''

#convert the string to float type(method 2)
def str2float(s):
	def fn(x, y):
		return 10 * x + y
	n = s.index('.')
	list0 = list(map(int, s[:n]))
	list1 = list(map(int, s[n+1:]))
	return reduce(fn, list0) + reduce(fn, list1) / 10**len(list1)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')	