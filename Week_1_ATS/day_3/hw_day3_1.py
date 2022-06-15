number = int(input("Enter a 5-digit integer: "))

i = 0
digits = []

for _ in range(0, 5):
    digits = [(number % 10)] + digits
    number = int(number / 10)

# print(digits)

if digits[0] == digits[4] and digits[1] == digits[3]:
    print(f"The number you entered is a palindrome")
else:
    print(f"The number you entered is NOT a palindrome")






