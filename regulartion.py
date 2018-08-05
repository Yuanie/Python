import re


test = input("Input the telephone number, I can tell you right or not:\n")
if re.match(r'^\d{3}\-\d{3,8}$', test):
	print("Yes")
else:
	print("No")



''' 切分字符串 '''

L = re.split(r'[\s\;\,]+', 'a, b,;c  d')
L1 = re.split(r'\s+', 'a b     c')
L2 = 'a b     c'.split(' ')
print(L)
print(L1)
print(L2)


''' 贪婪匹配 '''

print(re.match(r'^(\d+)(0*)$', '1023000').groups())		#\d+采用贪婪匹配，
print(re.match(r'^([1-9]{2})(0*)$', '12000').groups())
print(re.match(r'^(\d+?)(0*)$', '1023000').groups())  #\d+?就成为非贪婪匹配



''' 分组(group()) '''

m = re.match(r'^(\d{3})\-(\d{3,8})$', '010-12345')	#()表示提取的分组
print(m.groups())
print(m.group(0))	#原始字符串
print(m.group(1))	#第一个子串
print(m.group(2))	#第二个字串


#预编译
#re_date = re.compile(r'^(0[1-9]|1[0-2]|[0-9])\-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$')




