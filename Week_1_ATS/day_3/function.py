def func(x: int) -> int:
    return x ** 2

print(func(3.0))  

# positional arguments
# strict type in Python: def function(var_name: datatype) -> returnType
# *args must be specified before **kwargs

# Named Params
def func2(a:int = 0, b:int = 1) -> int:
    return a + b

print(func2(1, 3.0))

# exercise 1
def find_modulus(a=0, b=0):
    return a % b

# print(find_modulus({"a": 2, "b": 3}))


def add_infinite_nums(*y):
    sum = 0
    for i in y:
        sum += i
    return sum

print(add_infinite_nums(9, 4, 6, 8))

def student_details(**students):
    for key, value in students.items():
        print(f"{key}: {value}")
      

print(student_details(name = "Ahmad", age = 24, gender = "Male"))

a = [2,3,4]
ind = [0,1,2]

for i in enumerate(a):
    print(i)