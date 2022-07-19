import random
import sys

start = sys.argv[1]
end = sys.argv[2]

answer = random.randint(int(start), int(end))
while True:
    try:
        guess = int(input(f'Guess a number between {start}~{end}: '))
        if 0 < guess < 11:
            if guess == answer:
                print('You\'re a genius!')
                break
            elif guess > answer:
                print('Guess greater than random number')
                continue
            else:
                print('Guess lesser than random number')
                continue
        else:
            print('Hey bozo, I said 1~10')
            continue
    except ValueError:
        print('Please enter a number!')
        continue