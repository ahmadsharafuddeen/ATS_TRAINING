# Function that determines prime numbers
from math import sqrt


# Method 1 - n/2 as upper bound
def is_prime(number):
    if number == 1:
        return False
    flag = [1, number]
    
    for i in range(1, int(number / 2)):
        if number % i == 0 and i not in flag:
            return False
    return True

prime_nums = []
for i in range(1, 1001):
    if is_prime(i):
        prime_nums.append(i)
        # print(i)
        
print("Method 1: ")       
print(prime_nums)

# Method 2 - sqrt of number as upper bound
def is_prime2(number):
    if number == 1:
        return False
    flag = [1, number]
    
    for i in range(1, int(sqrt(number)) + 1):
        if number % i == 0 and i not in flag:
            return False
    return True

prime_nums2 = []
for i in range(1, 1001):
    if is_prime2(i):
        prime_nums2.append(i)
        # print(i)
 
print("Method 2: ")       
print(prime_nums2)