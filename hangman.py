import random
import string

guesses = 8
count = 0
win = False
guessed_letters = []

def choose_word():

    f = open('wordlist.txt', 'r')
    wordlist = list(f)
    word = random.choice(wordlist)
    f.close()
    return word

def guess_letter():

    guess = input("Guess a letter: ")

    while True:
        if guess not in string.ascii_lowercase or len(guess) > 1 or guess == '':
            guess = input("ERROR: Please enter a single letter: ")
        else:
            break
    return guess

word = choose_word()
word = word[:-1]
tempword = []
for i in word:
    tempword.append("_")
print(tempword)
print()


while count < guesses and not win == True:
    if '_' not in tempword:
        print('YOU WIN!')
        win = True
        break
    guess = guess_letter()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                tempword[i] = guess
        print("Correct!")
        print('---------------------------------')
        print(tempword)
        guessed_letters.append(guess)
        print("Guessed letters: ", guessed_letters)
        print("Guesses left: ", (8 - count))
        print('---------------------------------')
    else:
        print("Wrong!")
        print('---------------------------------')
        guessed_letters.append(guess)
        print(tempword)
        print("Guessed letters: ", guessed_letters)
        print("Guesses left: ", (7 - count))
        print('---------------------------------')
        count+=1
print("Word is", word)