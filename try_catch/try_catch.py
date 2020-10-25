"""
Dictionary
* try except playground
📚 Resources:
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1s&ab_channel=freeCodeCamp.org
"""

try:
    number = int(input('Enter a number: '))
    print(number)
except ZeroDivisionError:
    print('Divided by zero')
except ValueError:
    print('Invalid input')
