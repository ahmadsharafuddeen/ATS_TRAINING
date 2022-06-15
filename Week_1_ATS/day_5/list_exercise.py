def sep_list(str_list):
    if str_list == None:
        return str_list
    else:
        for word in str_list:
            print(word, end='')
            if word != str_list[-1]:
                print(", ", end='')
            
            
sep_list(['Ahmad', 'Adeniyi', 'Sharafudeen'])

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

COLUMN = 6
ROW = 9
new_grid = []
for x in range(ROW):
    row = []
    for y in range(COLUMN):
        print(grid[x][y], end='')