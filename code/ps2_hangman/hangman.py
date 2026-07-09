# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    count=0
    for i in secret_word:
      if(i not in letters_guessed):
        count+=1
    return count==0 


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    result=""
    for i in secret_word:
      if(i in letters_guessed):
        result+=i
      else:
        result+="*"
    return result
    


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    result=""
    alphabet=string.ascii_lowercase

    for i in alphabet:
      if( i not in letters_guessed):
        result+=i
    return result


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    allowed_characters=string.ascii_lowercase
    points=10

    def check_is_vowel(letter):
      """
      letter: string, letter that will be compared

      returns: number, represents a number that depends on whether the letter is a vowel or not. 2 if it is, 1 if it is not.
      """
      vowels="aeiou"
      return 2 if letter in vowels else 1
    def get_letter_not_guessed(secret_word, guessed_letters):
      """
      secret_word: string, the lowercase word the user is guessing
      guessed_letters: list (of lowercase letters), the letters that have been guessed so far
      
      returns: string, contain the letters that have not been guessed.
      """

      result=""
      for i in secret_word:
        if(i not in guessed_letters):
          result+=i
      return result

    def get_number_unique_letters(secret_word):
      string=""
      for i in secret_word:
        if(i not in string):
          string+=i
      return len(string)

    welcome_message=f"Welcome to hangman!"
    description=f"I am thinking of a word that is {len(secret_word)} letters long."
   
    print(welcome_message)
    print(description)

    list_guessed_letters=[]
    result=False
    available_characters=get_available_letters(list_guessed_letters)
    word_progressing=get_word_progress(secret_word,list_guessed_letters)

    while points>0 and result!=True:
      print("--------------")
      print(f"You have {points} guesses left.")
      print(f"Available letters: {available_characters}")
      guessing_word=input("Please guess a letter: ")

      if(guessing_word=="!" and with_help):
        if(points>3):
          letters_not_guessed= get_letter_not_guessed(secret_word,list_guessed_letters)
          random_index=random.randint(0,len(letters_not_guessed)-1)
          new_letter=letters_not_guessed[random_index]
          list_guessed_letters+=[new_letter]
          word_progressing=get_word_progress(secret_word,list_guessed_letters)
          points-=3
          print(f"Letter revealed: {new_letter}")
          print(word_progressing)
        else:
          print(f"Oops! Not enough guesses left: {word_progressing}")
      elif(guessing_word not in allowed_characters):
        print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {word_progressing}")

      elif(guessing_word not in available_characters):
        points-=check_is_vowel(guessing_word)
        print(f"Oops! You've already guessed that letter: {word_progressing}")
      elif(guessing_word in secret_word):
        list_guessed_letters+=[guessing_word]
        word_progressing=get_word_progress(secret_word,list_guessed_letters)
        available_characters=get_available_letters(list_guessed_letters)
        print(f"Good guess: {word_progressing}")
      else:
        points-=check_is_vowel(guessing_word)
        list_guessed_letters+=[guessing_word]
        available_characters=get_available_letters(list_guessed_letters)
        print(f"Oops! That letter is not in my word: {word_progressing}")

      total_score=(points+4*get_number_unique_letters(secret_word))+(3*len(secret_word))

      if(points<=0):
        print(f"-------")
        print(f"Sorry, you ran out of guesses. The word was {secret_word}")
        break

      checkWord= has_player_won(secret_word,list_guessed_letters)
      if(checkWord):
        result=True
        print("--------------")
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {total_score}")
        break



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    # pass   

