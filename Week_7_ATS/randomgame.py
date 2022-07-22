import random
import sys

start = input('Enter start: ')
end = input('Enter end: ')


def within_range(guess):
    return 0 < guess < 11

def is_correct(guess, answer):
    if within_range(guess):
        return guess == answer
    return False
    
if __name__ == '__main__':
    answer = random.randint(int(start), int(end))
    while True:
        try:
            guess = int(input(f'Guess a number between {start}~{end}: '))
            if within_range(guess):
                if is_correct(guess, answer):
                    print('You\'re a genius!')
                    break
                elif guess > answer:
                    print('Guess greater than random number')
                    continue
                else:
                    print('Guess lesser than random number')
                    continue
            else:
                print()
                continue
        except ValueError:
            print('Please enter a number!')
            continue