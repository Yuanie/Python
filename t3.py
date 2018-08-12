'''def normalize(name_list):
	name_list = name_list[0].upper() + name_list[1:].lower()
	return name_list
	
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)'''
#''' code segment ''' 多行注释

from functools import reduce 
def prod(L):
	return reduce(lambda x,y : x * y, L)

print('3 * 5 * 7 * 10 =', prod([3, 5, 7, 10]))
if prod([3, 5, 7, 10]) == 1050:
    print('测试成功!')
else:
    print('测试失败!')
	
	