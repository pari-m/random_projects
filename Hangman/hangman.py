import random

print('H A N G M A N')

list = ['python', 'java', 'kotlin', 'javascript']

random.shuffle(list)

computed_word = list[0]

word = input('Guess the word:')

print('You survived!' if word == computed_word else 'You are hanged!')
