from itertools import count


def count_down(n):
    print(n)
    if n > 0:
        n = count_down(n - 1)
# count_down(89)

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))

def fibonnaci(n):
    if n == 0 or n == 1:
        return 1
    return fibonnaci(n - 2) + fibonnaci(n - 1)

print(fibonnaci(10))
    