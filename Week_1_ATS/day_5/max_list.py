def find_max(num_list):
    max_num = 0

    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([34,87, 91, 32,76]))

