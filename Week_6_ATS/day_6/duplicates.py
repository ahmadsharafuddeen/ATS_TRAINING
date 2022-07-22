# todo: generate 20 random numbers

# random_nums = {key:value f}

# num = 2 if 4 > 3 else 5

# is_friend = False

# can_message = 'Message Allowed' if is_friend else 'Message not allowed'

# print(can_message)

# for i, char in enumerate(list(range(100))):
#     if char == 50:
#         print(f'The index of 50 is {i}')

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

fill = '*'
empty = ' '
for row in picture:
    for pixel in row:
        if pixel:
            print(fill, end='')
        else:
            print(empty, end='')
    print('')
    