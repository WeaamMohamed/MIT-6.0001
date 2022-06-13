# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)\
    
import string
import random


WORDLIST_FILENAME = "words.txt"



def draw_hang_man(mistake):
    """
   return:None, draw hang man each level
    parameter: mistake, int number of mistakes user did 
    """
    all_man = ['o','/', '|','\\' , '/','\\']
    
    only_draw = [' '] * len(all_man)
    for i in range(mistake):
        only_draw[i] = all_man[i]

      



    print(f'''

     ____
    |    |
    {only_draw[0]}    |
   {only_draw[1]}{only_draw[2]}{only_draw[3]}   |
   {only_draw[4]} {only_draw[5]}   |
         |
      ========
      
      ''')
  
"""


     ____
    |    |
    O    |
   /|\   |
   / \   |
         |
      ========

      
     """
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for secret_char in secret_word:
        if secret_char not in letters_guessed:
            return False
    return True




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    # only show the successful guessed characters otherwise use undersore 
    actual_word = ['_ '] * len(secret_word)
        
    for guessed_char in letters_guessed:
        for index, secret_char in enumerate(secret_word):
            if guessed_char == secret_char:
                actual_word[index] = secret_char
           
    #join to turn list into string 
    return ''.join(actual_word)




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed. '''
      
    #to get a string of all alphabet lower case characters 
    alphabet = string.ascii_lowercase
    # each element contain one character from alphabet 
    alphabet_list = list(alphabet)

    for letter in letters_guessed:
        if letter in alphabet_list:
            # hint: remove function mutates the list so no value returned to be assigned to new list. 
            alphabet_list.remove(letter)
            
    # join to turn list of char into string 
    return ''.join(alphabet_list)
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    print(f'''
Welcome to the game Hangman!    
I am thinking of a word that is {len(secret_word)} letters long.
-----------------------------''')
#You have 6 guesses left and 3 warnings
#Available letters: abcdefghijklmnopqrstuvwxyz''')
          

    #todo: check if user enter empty string or more than one character 
    


    num_guesses_left = 6
    mistakes = 0
    letters_guessed  = list()
    draw_hang_man(0)
    warnings = 3
    
    #print(f"You have {num_guesses_left} guesses left")
    #print("Available letters: ", get_available_letters(letters_guessed), end = " ")
    
    while(True):

        
        if num_guesses_left <= 0 :
            ##print("You consume all your guesses. ")
            break
        
        print(f"You have {num_guesses_left} guesses left")
        print("Available letters:", get_available_letters(letters_guessed), end = " ")
        letter_input = input("guess a letter: ")
        if not str.isalpha(letter_input):
            if warnings <= 0: 
                num_guesses_left -=1
                mistakes +=1
                draw_hang_man(mistakes)
            else:
                warnings -=1
            print(f"\nOops! That is not a valid letter... You have {warnings} warnings left\n")
            continue
        elif  len(letter_input) != 1:
            if warnings <= 0: 
                num_guesses_left -=1
                mistakes +=1
                draw_hang_man(mistakes)
            else:
                warnings -=1
            print(f"\nOops! letter must be one character try again... You have {warnings} warnings left \n")

            continue
        
        elif letter_input in letters_guessed:
            if warnings <= 0: 
                num_guesses_left -=1
                mistakes +=1
                draw_hang_man(mistakes)
            else:
                warnings -=1
            print(f"\nOops! You've already guessed that letter... You have {warnings} warnings left \n")
            continue
        
        else:
            num_guesses_left -=1
            letter_input = str.lower(letter_input)
            #if letter_input not in secret_word:
               # draw_hang_man(mistakes + 1) 
            




        letters_guessed.append(letter_input)
        result_guessed = get_guessed_word(secret_word, letters_guessed)

        if is_word_guessed(secret_word, letters_guessed):
            print("\n")
            break 
        
        if letter_input in secret_word:
            draw_hang_man(mistakes)
            print("Good guess:", result_guessed)
            
        else:
            mistakes+=1
            draw_hang_man(mistakes)
            print("Oops! That letter is not in my word:",result_guessed)

            
        print("--------------------\n")
            
        
    print('your guessed list: ', letters_guessed)
    print('Remaining guesses : ', num_guesses_left)
    
    if is_word_guessed(secret_word, letters_guessed):
        #Total score = guesses_remaining* number unique letters in secret_word
        total_score = num_guesses_left * len(letters_guessed)
        print(f"congratulates! you have guessed the word {result_guessed} correctly. \n"+ 
              f"Your score is: {total_score}")
        return
    else:
        print("Failed!!!!!!!!")
        return
        
        

    pass

 


def get_user_input(warnings):
    
    letter = input("guess a letter: ")

    if len(letter) != 1:
        warnings -=1
        print(f"Oops! letter must be one character try again... You have {warnings} warnings left ") 
        #get_user_input(warnings)
        return str.lower(letter), -1
        
        
    if not str.isalpha(letter):
        warnings -=1
        print(f"Oops! That is not a valid letter... You have {warnings} warnings left")
        #get_user_input(warnings)
        return str.lower(letter), -1
        
    return str.lower(letter), warnings
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    secret_word = "tact"
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)

#random_index =  random.randint(0, len(wordlist))
#secret_word = wordlist[random_index]
#secret_word = 'apple'
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's', 's', 'p']
#hangman(secret_word)
#@print("======================")
#print(secret_word)
#print("is word guessed:",is_word_guessed(secret_word, letters_guessed) )
#print("get guessed word:",get_guessed_word(secret_word, letters_guessed) )
#print('available letters:',get_available_letters(letters_guessed))




