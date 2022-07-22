# username = input('Username: ')
# password = input('Password: ')

# password_length = len(password)

# print(f"{username}, your password {'*' * password_length} is {password_length} letters long")

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
        
duplicates = list(set([letter for letter in some_list if some_list.count(letter) > 1]))
print(duplicates)

# def highest_even(li):
#     all_evens = []
#     for number in li:
#         if number % 2 == 0:
#             all_evens.append(number)
#     return max(all_evens)
# print(highest_even([10,2,3,4,8,11]))

# print("hello"[0])