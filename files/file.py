"""
Dictionary
* Read file playground
* Write file playground
📚 Resources:
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1s&ab_channel=freeCodeCamp.org
"""

# Read file
test_file = open('./files/test.txt', 'r')

print(test_file.readable())
# Read a single line
print(test_file.readline())
# Read all the lines
print(test_file.readlines())
test_file.close()


# Write a new file
new_test_file = open('./files/test.txt', 'w')
new_test_file.write('Some more test')
new_test_file.write('\nNext line')
new_test_file.close()

# Append to a file
append_test_file = open('./files/test.txt', 'a')
append_test_file.write('Some more test')
append_test_file.write('\nNext line')
append_test_file.close()