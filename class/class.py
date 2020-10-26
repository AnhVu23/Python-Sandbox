"""
Dictionary
* Class playground
* Object playground.
📚 Resources:
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1s&ab_channel=freeCodeCamp.org
"""


# Define and declare class
class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def get_name(self):
        return self.name


# Create new student object
student_1 = Student('Tom', 'IT', 8.0, True)
student_2 = Student('John', 'Business', 6.0, False)

print(student_1)
print(student_1.get_name())