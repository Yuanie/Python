import time,functools
def metric(fn):
	@functools.wraps(fn)
	def wrapper(*args, **kw):
		print('call %s()' % fn.__name__)
		t1 = time.time()
		func = fn(*args, **kw)
		t2 = time.time()
		print('%s executed in %s ms' % (fn.__name__, t2 - t1))
		return func
	return wrapper
	

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
print('fast(11, 22) = %s' % f)
s = slow(11, 22, 33)
print('slow(11, 22, 33) = %s' % s)

if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')