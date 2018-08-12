L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):			#按名字排序
	return t[0]
	
L2 = sorted(L, key = by_name)		#key指定的函数将作用于list的每一个元素上
#并根据key函数返回的结果进行排序
print(L2)


def by_score(t):		#成绩从高到低排序
	return -t[1]

L2 = sorted(L, key = by_score)
print(L2)