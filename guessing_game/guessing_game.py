"""
Dictionary
* Guessing game using while loop
📚 Resources:
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1s&ab_channel=freeCodeCamp.org
"""

secret_word = 'Simba'
guess = ''
numberOfGuess = 0
guessLimit = 3
out_of_guesses = False
while guess != secret_word and not out_of_guesses:
    guess = input('What is your favorite cartoon character? ')
    numberOfGuess += 1
    out_of_guesses = numberOfGuess >= guessLimit

if out_of_guesses:
    print('You lose')
else:
    print(f'Your number of guesses: {numberOfGuess}')
    print('Gotcha!')