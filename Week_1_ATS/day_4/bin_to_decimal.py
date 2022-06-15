bin_number = int(input("Enter a binary number: "))

bin_digits = []

while bin_number > 0:
    bin_digits = [bin_number % 10] + bin_digits
    bin_number = int(bin_number / 10)

print(bin_digits)

accumulator = 0  # contains the final result
i = 1   # positional value for each bin digit
len_bin = len(bin_digits) - 1
while len_bin >= 0:
    accumulator += bin_digits[len_bin] * i
    i *= 2
    len_bin -= 1

print(accumulator)


