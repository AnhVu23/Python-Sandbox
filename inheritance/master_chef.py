"""
Dictionary
* Inheritance playground
📚 Resources:
https://www.youtube.com/watch?v=rfscVS0vtbw&t=1s&ab_channel=freeCodeCamp.org
"""

from chef import Chef


class MasterChef(Chef):

    def make_fine_dining(self):
        print('Make fine dining dish')


master_chef = MasterChef('Tom')
print(master_chef.name)
print(master_chef.make_chicken())