"""
Dictionary
* Nested loop playground
* 2D Lists playground
📚 Resources:
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1s&ab_channel=freeCodeCamp.org
"""

# 2D List
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][1])
print(number_grid[2][1])

# Nested loops
for row in number_grid:
    for col in row:
        print(col)