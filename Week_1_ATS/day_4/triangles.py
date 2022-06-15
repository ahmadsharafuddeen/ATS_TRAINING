for i in range(1, 11): 
    print('* ' * i)

print()

for i in range(10, 0, -1):
    print('* ' * i)


for i in range(1, 11):
    for j in range(1, 11):
        if j <= 10 - i:
            print(' ', end = ' ')
        else:
            print('*', end = ' ')
    print()

