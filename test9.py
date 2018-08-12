def fib(max):
	a, b, n = 0, 1, 0
	while n < max:
		yield b
		a, b = b, a + b
		n += 1
	return 'done'		#generater 取不到其返回值，需捕获StopIteration错误

	
g = fib(10)	
print(g)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break

		