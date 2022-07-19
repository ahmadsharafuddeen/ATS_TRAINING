def fib(number):
    a = 0
    b = 1
    for _ in range(number):
        yield a
        temp = a
        a = b
        b = temp + b
        
for i in fib(20):
    print(i)