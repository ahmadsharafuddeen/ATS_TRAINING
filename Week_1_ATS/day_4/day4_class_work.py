# vowels rep. with special characters
vowels = {"a": "#", "e": "$", "i": "%", "o": "&", "u": "*", "A": "#", "E": "$", "I": "%", 
"O": "&", "U": "*"}
consonants = {"0": "z", "1": "y", "2": "x", "3": "w", "4": "v", "5": "t", "6": "s", "7": "r", "8": "q", 
"9": "p"}
special_chars = ["@", "_", "!", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "?", "/", "\\", "|", "}",
"{", "~", ":"]

# user_input = input("Enter the string to encode: ")


def encode_text(user_input):
    split_input = list(user_input)
    encoded = ""
    for char in split_input:
        if char in list(vowels.keys()):
            encoded += vowels[char]
        elif char in list(consonants.keys()):
            encoded += "^" + consonants[char]
        elif char.isalpha():
            encoded += char.upper()
        elif char in special_chars:
            encoded += "|" + char
    return encoded


print(encode_text("adeola"))

encoded_text = input("Enter the encoded text: ")
# def decode_text():
split_input = list(encoded_text)
decoded = ""

# for i in range(0, len(split_input) - 1):
#     key = [k for k, v in vowels.items() if v == split_input[i]]
#     # decode special chars with mapped vowels
#     if split_input[i] == '|':
#         continue
#     elif split_input[i] in special_chars and split_input[i - 1] == '|':
#         decoded += split_input[i]
#     elif key[0] in list(vowels.values()):
#         decoded += key[0]
#     # eli
    

# print(decoded)?

# if char in list(vowels.keys()):
#             encoded += vowels[char]
#         elif char in list(consonants.keys()):
#             encoded += "^" + consonants[char]
#         elif char.isalpha():
#             encoded += char.upper()
#         elif char in special_chars:
#             encoded += "|" + char
#     return encodedi








