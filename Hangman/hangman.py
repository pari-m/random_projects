# Write your code here
import random

print('H A N G M A N\n')

wlist = ['python', 'java', 'kotlin', 'javascript']
random.shuffle(wlist)

computed_word = wlist[0]

#sub_word = computed_word[:3] + "-" * (len(computed_word)-3)
temp_word= len(computed_word) * '-'

computed_word_with_blanks = list(temp_word)

correctely_guessed_words = list()
word_aldready_guessed = 0
first_word_guess = 0

no_of_attempts = 0



while no_of_attempts < 8:
    letter_present = 1
    no_of_attempts += 1
    if first_word_guess == 1:
        no_of_attempts += -1
    first_word_guess = 0
    word_aldready_guessed = 0
    print(*computed_word_with_blanks,sep = "")
    letter = input('Input a letter:')
    for i in range (0,len(computed_word)):
        if letter not in computed_word:
            letter_present = 0
            if no_of_attempts == 8:
                print("No such letter in the word")
                break
            break
        if computed_word[i] == letter:
            letter_present = 1
            word_aldready_guessed = 1
            for j in range (0,len(computed_word)):
                if computed_word[j] == letter:
                    computed_word_with_blanks[j] = letter
            if letter in correctely_guessed_words:
                print("No improvements")
                break
            if letter not in correctely_guessed_words and first_word_guess != 1:
                first_word_guess = 1
                correctely_guessed_words.append(letter)
                break
            if letter not in correctely_guessed_words:
                correctely_guessed_words.append(letter)
                break
        if computed_word[i] == letter and no_of_attempts == 8:
            print("No improvements")
            break            

    if letter_present == 0:
        print("No such letter in the word")
    if list(computed_word) == computed_word_with_blanks:
        break
    if no_of_attempts == 8:
        print("You are hanged!")
        break
    print()


if list(computed_word) == computed_word_with_blanks:
    print()
    print(f'{computed_word} \nYou guessed the word!\nYou survived!')
