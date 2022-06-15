import string
import time

# Constants Declaration
digits = string.digits
s_char = string.punctuation
alpha_lower = string.ascii_lowercase
alpha_upper = string.ascii_uppercase
rev_alpha_lower = alpha_lower[::-1]

# Vowels mapping secret
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_map = ['#', '$', '%', '&', '*']

def encode(data: str):
    enc = list()
    for s in data:
        if s.lower() in vowels:
            enc.append(vowels_map[vowels.index(s.lower())])
        elif s in s_char:
            enc.append('|' + s)
        elif s in alpha_lower + alpha_upper:
            enc.append(s.swapcase())
        elif s in digits:
            enc.append('^' + rev_alpha_lower[digits.index(s)])
    return "".join(enc)

print(f"Encoded: {encode('~ahm!24')}")

def decode(data: str):
    dec = list()
    strange_chars = ['|', '^']
    strange = ''
    for s in data:
        if strange != '':
            if strange == '|':
                dec.append(s)
                strange = ''
            elif strange == '^':
                dec.append(str(rev_alpha_lower.index(s)))
                strange = ''
        elif s in strange_chars:
            strange = s
            continue
        elif s in vowels_map:
            dec.append(vowels[vowels_map.index(s)])
        elif s in alpha_lower + alpha_upper:
            dec.append(s.swapcase())
    return "".join(dec)

print(f"Decoded: {decode('|~#HM|!^x^v')}")
        