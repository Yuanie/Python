grade = {}
homepage = input('welcome to the center of health! press any key to continue\n')
while True:
	print ('~~\nwelcome\n~~')
	menu = ('1.sign in', '2.check', '3.modify', '4.delete', '5.preview', '6.exit')
	for feature in menu:
		print(feature)
	number = ('1','2','3','4','5','6')
	order = input('please input your number:\n')
	if order in number:
		num = int(order)
		while num == 1:
			name = input('input the student name:\n')
			height = float(input('input the student height(M):'))
			weight = float(input('input the student weight(Kg):'))
			BMI = weight / (height **2)
			grade[name] = BMI
			exit = input('succeed!press any key to continue,press Y to return\n')
			if upper(exit) == 'Y':
				break
			else:
				continue
		
