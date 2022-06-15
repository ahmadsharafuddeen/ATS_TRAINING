# Factorial Program [3.6 a]
def factorial(num):
    fact = 1
    if num < 0:
        return "No factorial for negative numbers!"
    elif num == 0:
        return "The factorial of Zero is One"
    elif num >= 1:
        for i in range(1, num + 1):
            fact *= i
    return fact

new_list = ['Ahmad', 'Adeniyi']
new_list.append('Sharafudeen')
print(new_list)




    
