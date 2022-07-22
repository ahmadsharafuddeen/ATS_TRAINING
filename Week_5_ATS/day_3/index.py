import random
from re import I

rand_dict = {index:random.randint(1, 99) for index in range(1, 21)} 
print(rand_dict) 

rand_values = list(rand_dict.values())

duplicates = set([item for item in rand_values if rand_values.count(item) > 1]) 
print(duplicates)

# generators

def generate_numbers(num):
    for i in range(num):
        yield i * 2
        
for i in generate_numbers(100):
    print(i)