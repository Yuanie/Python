def count_words(filename):
	''' 计算一个文件大致包含多少个单词 '''
	try:
		with open(filename, 'r', encoding = 'UTF-8') as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		print("This file " + filename + " does not exist.")
	else:
		# 计算文件的单词数
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")
		
filename = ['alice.txt', 'moby_dick.txt', 'little_women.txt']
for name in filename:
	count_words(name)
		