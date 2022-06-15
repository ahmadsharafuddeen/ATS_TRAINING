def print_list(some_list):
    
    i = 0
    while i < len(some_list):
        if int(some_list[i]) % 2 == 0:
            print(some_list[i])
        if int(some_list[i]) % 3 == 0:
            print(int(some_list[i]) % 3)
        i += 1
   
    
            
print(print_list([1, '2', 3, '4', 5, '6']))



# print(6 % 3)
