import functools
def log(text):
	def decorater(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper 
	return decorater

	
@log('execute')
def now():
	print('2018-07-23')
	
now()
print(now.__name__)
