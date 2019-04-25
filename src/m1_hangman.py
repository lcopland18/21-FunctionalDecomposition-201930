"""
Make separate display function to show dashes call list (fix check function)
Min length of mystery word
Finish hangman
"""

"""
Hangman.

Authors: Lauren Copland and Justin Guilfoyle.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

import random
def main():
    # test_random_word()
    # guess()
    # test_check()
    #test_guess_check()
    loop()
def random_word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
        r = random.randrange(0,len(words))
        item = words[r]
        return item

def test_random_word():
    word = random_word()
    print(word)

def guess():
    letter = str(input('Guess Letter Here: '))
    return letter

def check(word, guess):
    dashes = []
    for k in range(len(word)):
        dashes.append('-')
    print(dashes)

    for k in range(len(word)):
        if word[k] == guess:
            print('Your guess was correct')
            dashes[k] = word[k]
            print(dashes)
            return 0
    print('Your guess was incorrect')
    print(dashes)

    return 1

def test_check():
    expected = 'Your guess was correct'
    actual = check('hello','e')

    expected = 'Your guess was incorrect'
    actual = check('hello','j')

def guess_check():
    word = random_word()
    g = guess()
    check(word, g)
    print(word) # Get rid of in final version

def test_guess_check():
    guess_check()

def lives():
    life = int(input('How many guesses do you want?'))
    return life

def reset():
    print('Play again?')
    response = str(input('y/n'))
    if response == 'y':
        hangman()
    if response =='n':
        print('Thanks for playing hangman')
        print('Did this end?')


def loop():
    life = lives()
    count = 0
    word = random_word()
    correct = []
    incorrect = []

    while count < life:
        letter = guess()
        returned = int(check(word, letter))

        if returned == 0:
            correct.append(letter)

        else:
            incorrect.append(letter)
            count += 1

        print("Correct guesses",correct, "Incorrect Guesses", incorrect)

        if len(correct) == len(word):
            print('You Win!')
            reset()

        elif life == len(incorrect):
            print('You lose')
            reset()

def hangman():
    print('I will choose a random secret word from a dictionary. You set the minimum length of that word.')
    print()
    print('You set the difficulty of the game by setting the number of unsuccessful choices you can make before you lose the game. The traditional form of hangman set this to 5.')
    min_length()
    loop()


main()

