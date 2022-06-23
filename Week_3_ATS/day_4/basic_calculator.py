import pyinputplus as pyip


operation = pyip.inputChoice(prompt='''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''', choices=['+', '-', '*', '/'])

first_num = pyip.inputNum(prompt="Enter the first number: ")
second_num = pyip.inputNum(prompt="Enter the second number: ")

if operation == '*':
    print(f"{first_num} {operation} {second_num} = ")
    print(first_num * second_num)
elif operation == '/':
    print(f"{first_num} {operation} {second_num} = ")
    print(first_num / second_num)
elif operation == '+':
    print(f"{first_num} {operation} {second_num} = ")
    print(first_num + second_num)
elif operation == '-':
    print(f"{first_num} {operation} {second_num} = ")
    print(first_num - second_num)