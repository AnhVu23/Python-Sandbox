"""
Dictionary
* List playground
📚 Resources:
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1s&ab_channel=freeCodeCamp.org
"""
# List of friends
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim']
my_friend = friends[1]

# Update an item in array
friends[1] = 'Mike'
print(my_friend)
print(friends)
print(friends[1])

# Choose a range in array
print(friends[1:2])
print(friends[1:3])

# Extend lists
friends.extend(lucky_numbers)
print(friends)

# Append (add item at the end of the list)
friends.append('Johny')
print(friends)

# Insert (add item at a specific index of the list)
friends.insert(1, 'Kelly')
friends.insert(3, 'Tom')
print(friends)

# Find index of item
print(friends.index('Kelly'))

# Remove item
friends.remove('Jim')
print(friends)

# Copy
friends2 = friends.copy()

# Count
print(friends.count('Tom'))

# Sort
lucky_numbers.sort()
print(lucky_numbers)

# Reverse
lucky_numbers.reverse()
print(lucky_numbers)

# Remove last item
friends.pop()
print(friends)

# Clear
friends.clear()
print(friends)