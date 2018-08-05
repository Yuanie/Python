#do slice to trip the space(method 1)
def trim(s):
	item1 = 0
	item2 = -1
	while item1 < len(s):
		if s[item1] == ' ':
			item1 += 1
		else:
			break 
	while item2 > -len(s):
		if s[item2] == ' ':
			item2 -= 1
		else:
			break
	
	return s[item1 : len(s) + item2 + 1]	

	
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')