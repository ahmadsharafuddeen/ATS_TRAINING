import sys

def collatz(number):
    if number % 2 == 0:
        calc = number // 2
        print(f"{number} is an even number")
        print(f"Result of {number}//2 = {calc}")
        return calc
    else:
        calc = 3 * number + 1
        print(f"{number} is an odd number")
        print(f"Result of 3 * {number} + 1 = {calc}")
        return calc

# collatz(10)
try:
    while True:
        result = collatz(int(input("Enter a number: ")))
        if result == 1:
            sys.exit()
except ValueError:
    print("You must enter only integer values!")



        
