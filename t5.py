def not_empty(s):		#将序列中的空字符串删除掉，注意bool('') 和 bool(None) 都为false
	return s and s.strip()

	
print(list(filter(not_empty, ['A', 'B', '', None, 'C', ' '])))
	
'''
#using filter to get prime 埃氏筛法
#filter 返回的是一个 Iterator,如果要强迫filter()完成计算结果，list()来获取一下

def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n 

def _not_divisible(n):
	return lambda x : x % n > 0
	
	
def primes():
	yield 2
	it = _odd_iter()	#初试序列
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)  #构造新序列
		
		
		
#primes 是无限序列，调用时需要设置一个退出条件
L = []
for n in primes():
	if n < 100:
		L.append(n)
	else:
		break

print(L)
'''