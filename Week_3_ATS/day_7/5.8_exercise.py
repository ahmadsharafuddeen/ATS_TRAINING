from multiprocessing.reduction import duplicate
from os import dup
import random

rand_nums = []

for i in range(20):
    gen = random.randint(1, 99)
    rand_nums.append(gen)
    
rand_nums.sort()  
  
print(rand_nums)

def find_duplicate(list):
    for i in range(19):
        if list[i] != list[i + 1]:
            continue 
        return f"There's duplicate {list[i]} in the list!"
    return "There's no duplicate in the loop"

print(find_duplicate(rand_nums))
    
