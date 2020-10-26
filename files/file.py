"""
Dictionary
* Read file playground
* Write file playground
📚 Resources:
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1s&ab_channel=freeCodeCamp.org
"""

# Read file
test_file = open('test.txt', 'r')

print(test_file.readable())
# Read a single line
print(test_file.readline())
# Read all the lines
print(test_file.readlines())
test_file.close()