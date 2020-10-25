"""
Dictionary
* Basic calculator application
* Transform string to float
📚 Resources:
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1s&ab_channel=freeCodeCamp.org
"""

num1 = float(input('Enter a number: '))
operator = input('Enter an operator: ')
num2 = float(input('Enter another number: '))


# Calculating result
def calculate(first_num, second_num, op):
    if op == '*':
        return first_num * second_num
    elif op == '-':
        return first_num - second_num
    elif op == '+':
        return first_num + second_num
    elif op == '/':
        return first_num / second_num
    else:
        return 'Invalid operator'


# Parsing and calculating result
result = calculate(num1, operator, num2)
print(result)