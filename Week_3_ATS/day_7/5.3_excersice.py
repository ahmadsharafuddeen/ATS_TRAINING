from ordinal_func import determine_ordinal 

numbers = []    
# read in 20 numbers
for i in range(1, 21):
    number = input(f"Enter the {determine_ordinal(i)} number: ")
    if number in numbers:
        print("Duplicate of the number already read!")
        continue
    print(number)
    numbers.append(number)