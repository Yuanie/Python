import json

numbers = [2, 3, 5, 6, 17]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)
#json.dump(要存储的数据，可用于存储数据的文件对象)
	
with open(filename) as f_obj:
	numbers = json.load(f_obj)
	
print(numbers)
