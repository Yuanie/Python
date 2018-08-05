import re

re_email1 = re.compile(r'^[0-9a-zA-z\.*]+\@[0-9a-zA-z\.*]+.com$')
re_email2 = re.compile(r'^\<?(\w+\s?\w+)\>?\s?\w*@\w+\.\w+$')
def is_valid_email(addr):
	if re_email1.match(addr):
		return True
	else:
		return False
	

assert is_valid_email('someone@gmail.com')		#assert condition  (if false,raise error)
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
		
		
		
		

def name_of_email(addr):
	if re_email2.match(addr).groups():
		return re_email2.match(addr).group(1)
	else:
		return None


assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')