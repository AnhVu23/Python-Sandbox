"""
Dictionary
* String playground
📚 Resources:
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1s&ab_channel=freeCodeCamp.org
"""
phrase = 'Giraffe Academy'
# Lower case
print(f'{phrase.lower()} is cool')
# Uppercase and check if the string is uppercase
print(f'{phrase.upper()} is more cool')
print(f'{phrase.upper().isupper()}')
# Find the length of string
print(f'Length of text: {len(phrase)}')
# Index of a substring
charIndex = phrase.index('ffe')
print(f'{charIndex}')
# String replace
replace = phrase.replace('Giraffe', 'Cat')
print(f'{replace}')
