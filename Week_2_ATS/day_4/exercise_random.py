from enum import unique
import random
from re import sub
import string


subjects = ['Ahmad', 'Ade', 'Kola',]# 'tailor', 'developer', 'boy', 'lady']
verbs = ['eats', 'reads', 'drives', ]#'read', 'greeted', 'carried']
objects = ['food', 'book', 'car', ]#'rice', 'cloth']

print(random.shuffle(subjects))

# def gen_sentence():
#     random.shuffle(subjects)
#     random.shuffle(verbs)
#     random.shuffle(objects)
    
    # return f"The {random.choice(subjects)} {random.choice(verbs)} the {random.choice(objects)}"
    

def gen_words(num: int):
    gen_sentences = []
          
    for _ in range(num):
        sentence = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}"
        if sentence not in gen_sentences or len(gen_sentences) != len(subjects) * len(verbs) * len(objects):
            gen_sentences.append(sentence)
            print(f"{sentence} {len(gen_sentences)}")
        else:
            print("No more sentences to generate")
            break
         
    return gen_sentences        

gen_words(27)