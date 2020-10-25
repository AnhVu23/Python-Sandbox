"""
Dictionary
* If/else condition
📚 Resources:
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1s&ab_channel=freeCodeCamp.org
"""

# Condition
is_male = True
is_tall = True
if is_male and is_tall:
    print('You are a male and you are tall')
elif is_male and not is_tall:
    print('You are a male and you are not tall')
elif not is_male and is_tall:
    print('You are not a male and you are tall')
else:
    print('You are neither a male nor tall')
