from itertools import count


def count_down(n):
    print(n)
    if n > 0:
        n = count_down(n - 1)
# count_down(89)

def fib(n):
    return 1 if n == 0 else n * fib(n - 1)

print(fib(5))