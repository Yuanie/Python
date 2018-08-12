import functools  #functools.partial可以固定住原函数的部分参数，从而使调用简单
int2 = functools.partial(int, base = 2)
max2 = functools.partial(max, 10, 12, 17)   

A = int2('10010')    #相当于 kw = {'base' : 2}  int('10010', **kw)
B = max2(5,6,7)     #10,12,17会作为*args的一部分自动加到左边

print(A , B)