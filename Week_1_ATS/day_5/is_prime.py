# function that determines perfect numbers
def is_perfect(number):
    positive_div = []
    if number < 0:
        return False
    for i in range(1, number):
        if number % i != 0:
            continue
        positive_div.append(i)
        
    print(f"Positive divisors of {number}: {positive_div}")
    return sum(positive_div) == number

# print(is_perfect(6))

# Function that determines prime numbers
def is_prime(number):
    if number == 1:
        return False
    flag = [1, number]
    
    for i in range(1, number + 1):
        if number % i == 0 and i not in flag:
            return False
    return True

print(is_prime(1))

        
        