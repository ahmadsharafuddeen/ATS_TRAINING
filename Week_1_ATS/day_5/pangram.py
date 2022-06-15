import string

all_letters = list(string.ascii_lowercase)

def pangram(string):
    list_str = list()
    for char in string:
        list_str.append(char.lower()) 
    for letter in all_letters:
        if letter not in list_str:
            print(letter)
            return False
    return True

print(pangram("Two driven jocks help fax my big quiz"))

# print(list("The quick brown fox jumps over the lazy dog"))


