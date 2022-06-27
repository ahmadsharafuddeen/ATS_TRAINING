from decimal import DivisionByZero
import pyinputplus as pyip


operation = pyip.inputChoice(prompt='''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''', choices=['+', '-', '*', '/'])

numbers = pyip.inputStr("Enter a comma-separated numbers to calculate: ")
cleaned_num = numbers.split(',')
# print(cleaned_num)

result = int(cleaned_num[0])
for i in range(1, len(cleaned_num)):
    if operation == '+':
        result += int(cleaned_num[i])
    if operation == '-':
        result -= int(cleaned_num[i])
    if operation == '*':
        result *= int(cleaned_num[i])
    if operation == '/':
        try: 
            result /= int(cleaned_num[i]) 
        except ZeroDivisionError:
            print("Cannot divide by Zero")
    
print(result)         