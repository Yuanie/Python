#判断回数（121，1331，1221等）
'''
from functools import reduce
digits = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, \
		'6' : 6,  '7' : 7, '8' : 8, '9' : 9}
def str2num(s):
	return digits[s]

def fn(x, y):
	return 10 * x + y 
	
def is_palindrome(n):
	if n < 10:
		return True
	else:
		s = str(n)
		L = list(map(str2num, s))
		n1 = reduce(fn, L)
		L.reverse()
		n2 = reduce(fn, L)
	return n1 == n2
'''

def is_palindrome(n):
	return str(n)[:] == str(n)[::-1]			#more simple way~~
	#[start end step]
	
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')