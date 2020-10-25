"""
Dictionary
* Dictionary playground
📚 Resources:
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1s&ab_channel=freeCodeCamp.org
"""

# Define a dictionary
monthConversions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sept': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'December': 'December',
}

print(monthConversions.get('Jan'))

# Return default string when there's no key-value pair matches the request
print(monthConversions.get('Luv', 'Not a valid key'))