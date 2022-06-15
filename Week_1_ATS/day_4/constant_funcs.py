from factorial import factorial

# Constant e formula [3.6 b]
def math_const(terms):
    constant_e = 1
    for i in range(0, terms + 1):
        constant_e += 1 / factorial(i)
    return constant_e

print(math_const(10))

# Constant e formula [3.6 c]
def math_exp(x, terms):
    constant_e = 1
    for i in range(1, terms + 1):
        constant_e += x ** i / factorial(i)
    return constant_e

# print(math_exp(2, 10))