


#斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    #return '此处的错误'
    #这个return会返回异常

g = fib(10)
while True:
     try:
         x = next(g)
         print('g:', x)
     except StopIteration as e:
         print('Generator return value:', e.value)
         break
'''
g: 1
g: 2
g: 3
g: 5
g: 8
g: 13
g: 21
g: 34
g: 55
Generator return value: None
'''