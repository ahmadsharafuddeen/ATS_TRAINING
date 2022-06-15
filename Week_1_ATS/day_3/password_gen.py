import random
import string

def password_generator(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    confusing_chars = ('O', '0', '1', 'l')
    password = ''
    while not len(password) == length:
        char = random.choice(chars)
        if char not in confusing_chars:
            password += char
    return password
print(string.ascii_letters)
print(password_generator(10))

name = "AHMAD"
surname = "SHARAFUDEEN"
# print("His name is {} {}".format(name, surname))

arr = [1,2,3,4,5]
rev_arr = arr[::-1]
print(rev_arr)