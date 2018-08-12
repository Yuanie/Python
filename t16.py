filename = 'guest_book.txt'

with open(filename, 'a') as file_object:
	while True:
		names = input("Enter your name: ")
		if names:
			print("welcome!" + names)
			file_object.write(names + "\n")
		else:
			break
		
	