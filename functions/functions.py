"""
Dictionary
* Functions playground
* Function with return statement
📚 Resources:
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1s&ab_channel=freeCodeCamp.org
"""


# Define a function
def say_hi(name, age):
    print(f'Hello user {name}, you are {str(age)}')


# Execute function
say_hi('Tom', 30)


# Define a function with return statement
def cube(num):
    return pow(3, num)


result = cube(3)
print(result)