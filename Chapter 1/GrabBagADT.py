"""
1.2 A Grab Bag ADT is similar to the Bag ADT with one difference. A grab
bag does not have a remove() operation, but in place of it has a grabItem()
operation, which allows for the random removal of an item from the bag.
Implement the Grab Bag ADT.
"""

import random

class GrabBag:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def grab_item(self):
        if len(self.items) == 0:
            raise ValueError("Grab bag is empty")
        index = random.randint(0, len(self.items) - 1)
        item = self.items.pop(index)
        return item

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
    

if __name__ == '__main__':
    grab_bag = GrabBag()
    grab_bag.add("apple")
    grab_bag.add("banana")
    grab_bag.add("orange")

    print("Bag Items: ", grab_bag)  # prints ['apple', 'banana', 'orange']

    item = grab_bag.grab_item()
    print("Grab one random item: ", item)  # prints a random item from the grab bag
    print("Bag after grabbing one item: ", grab_bag)  # prints the remaining items in the grab bag