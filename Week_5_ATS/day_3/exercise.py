from functools import reduce

# print([2000 + i for i in range(20)])

# functional programming in python - map, filter, reducex
result = list(map(lambda num: num * 2, [1,2,3,4]))
print(result)

# filter function
result = list(filter(lambda num: num % 2 != 0, [1,2,3,4,5,6]))
print(result)

# zip usernames and passwords
usernames = ['Ahmad', 'Shaakir', 'Zayd']
passwords = ['Adeniyi2022', 'Shaks21', 'Zayd05']
emails = ['ahmad@gmail.com', 'shaks@yahoo.com', 'zayd@gmail.com']
print(list(zip(usernames, passwords, emails)))

# reduce function
print(reduce(lambda acc, num: acc + num, [10,11,12,13,14,15], 5))


# function that multiply params
def multipy_nums(*args):
    return reduce(lambda acc, item: acc * item, args, 1)
    

print(multipy_nums(1,2,3,4,5))

# squared list with lambda
my_list = [5,4,3]
print(list(map(lambda item:item ** 2, my_list)))

# list sorting
a = [(0,2), (9,9), (4,3), (10,-1)]
print(sorted(a, key=lambda item: item[1]))

new_dict = [{'name': 'Ahmad', 'surname': 'Sharaf'}]

print(list(map(lambda dict: list(dict.keys()), new_dict)))

print('12-11'.split('-')[1])

print([num ** 2 for num in range(100) if num % 2 != 0])
print({char for char in 'Ahmad Sharafudeen'})
