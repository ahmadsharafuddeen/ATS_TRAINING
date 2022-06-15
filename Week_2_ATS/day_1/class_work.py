# CLASS WORK
# 1a 
import string

all_letters = string.ascii_lowercase
first_ten_letters = list(all_letters[:10])
print(first_ten_letters)


# 1b LAST 10 ELEMENTS
last_ten_elements = list(all_letters[-10::])
print(last_ten_elements)

# 1c English vowels
eng_vowels = ['a', 'e', 'i', 'o', 'u']
print(eng_vowels[2:4])

# 1d English consonants
eng_consonants = [x for x in all_letters if x not in eng_vowels]
print(eng_consonants)

number_of_vowels = len(all_letters) - len(eng_consonants)
print(f"Number of English vowels: {number_of_vowels}")

# 2 Lists of vowels and consonants
sort_letters = eng_consonants
sort_letters.extend(eng_vowels)
sort_letters.sort()
print(sort_letters)

# 3 determine word case
def determine_case(word):
    if word.isupper():
        print("The word is in uppercase")
    elif word.islower():
        print("The word is in lowercase")
    else:
        print("The word is in mixedcase")
        
determine_case('hmad')
        
# 4 dictionary
def dict_key(dict):
    for key, value in dict.items():
        print(f"{key} is the key. {value} is the value")
        
dict_key({"name": "Ahmad", "gender": "Male"})

# 5 determine odd numbers
num_list = [1,2,3,4,5]
num_list.extend([6,7,8,9,10])

for num in num_list:
    if num % 2 == 1:
        num_list.remove(num)
print(f"Remaining even numbers: {num_list}")


# dictionary of letters and index
dict_all_letters = {}
for index, letter in enumerate(all_letters, 1):
    dict_all_letters[letter] = index
    
print(dict_all_letters)
    
        
    
