import random
import re

# TODO: Get random word from hangman.txt
chosen_word = random.choice(open("./Week_3_ATS/day_4/hangman.txt").read().split()).strip()
print(chosen_word)

# TODO: PRINT blank lines that correspond to the length of word
generated = ['_' for _ in chosen_word]

def hangman_game():
    for rem_attempts in range(8, 0, -1):
        # TODO: Get user guessed letter
        guess = input(f"Guess a letter ({rem_attempts} tries remaining): ") 
        # TODO: check if guessed letter is in hangman word and replace
        if guess in chosen_word and guess not in generated and '_' in generated:
            indices = [i.start() for i in re.finditer(guess, chosen_word)]
            for index in indices:
                generated[index] = guess
            print(''.join(generated))
            # TODO: Determine if win / lose
            if '_' not in generated:
                return f"Congrats! You won after {8 - rem_attempts} attempts 😍😂"
            continue
        print(''.join(generated))
        print("Wrong Attempt! 🤨")
    return "Failed attempts. You lost! 😒😔"

print(hangman_game())

        

    

