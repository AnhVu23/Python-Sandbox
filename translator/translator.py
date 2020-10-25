"""
Dictionary
* Translator playground
📚 Resources:
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1s&ab_channel=freeCodeCamp.org
"""

vowel = ['a', 'e', 'i', 'o', 'u']


# Translate function: If letter is a vowel, we transform it to g
def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower() in vowel:
            translation = translation + 'g'
        else:
            translation = translation + letter
    return translation


print(translate(input('Enter a phrase: ')))
