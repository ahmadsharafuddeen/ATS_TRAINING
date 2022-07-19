import random

rand_dict = {}
for i in range(1, 21):
    rand_dict[f'{i}'] = random.randint(1, 99)
   
print(rand_dict) 
duplicates = []

# dict_values = list(rand_dict.values())
for i in range(1, 20):
    if rand_dict[f'{i}'] != rand_dict[f'{i + 1}']:
        continue
    duplicates.append(rand_dict[f'{i}'])
    
print(duplicates)