"""
Dictionary
* Exponent functions playground
📚 Resources:
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1s&ab_channel=freeCodeCamp.org
"""


# Exponent function
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(10, 3))
