
def print_hello(name, sex):
    sex_dict = {1: 'Mr.', 2: 'Miss '}
    print ('hello %s%s, welcome to python world!' %(sex_dict.get(sex), name))
	
print_hello('nieyuan', 1)
print_hello(sex = 2, name = 'pengting')
print_hello(name = 'wang')

