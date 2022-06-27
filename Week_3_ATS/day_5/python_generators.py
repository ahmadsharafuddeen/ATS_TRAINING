from asyncore import read


def loop():
    l = [1,2,3,4]
    for num in l:
        yield num
        
f = loop()  
for r in f:
    print(r)
        
# loop()

def read_file(name):
    for row in open(name, 'r'):
        yield row
        
read_file("/Week_3_ATS/day_5/hangman.txt")