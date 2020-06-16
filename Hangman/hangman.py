# Write your code here
import random

print('H A N G M A N \n')

wlist = ['python', 'java', 'kotlin', 'javascript']
random.shuffle(wlist) # shuffle the word list
 
computed_word = wlist[0] # Get the first element in the shuffled list

#sub_word = computed_word[:3] + "-" * (len(computed_word)-3)
temp_word= len(computed_word) * '-' # Create the blank pattern for guessing.

computed_word_with_blanks = list(temp_word)  # convert the pattern to a list


no_of_attempts = 0


while no_of_attempts < 8:
    letter_present = 1
    no_of_attempts += 1
    print(*computed_word_with_blanks,sep = "")   # Print the elements in the list without any space
    letter = input('Input a letter:')  # Get input from the user
    if letter in computed_word:
        for i in range (0,len(computed_word)):  # Check if character is part of the computer_word
            if computed_word[i] == letter and letter_present != 0: 
                computed_word_with_blanks[i] = letter  # if yes, replace the character in the list.
    else:
        print("No such letter in the word")  # if letter pesent = 0 print.

    print()  
        
        
print() 

print("Thanks for playing!")

print("We'll see how well you did in the next stage")