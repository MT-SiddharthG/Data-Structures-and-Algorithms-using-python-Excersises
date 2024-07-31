"""
1.3 A Counting Bag ADT is just like the Bag ADT but includes the numOf(item)
operation, which returns the number of occurrences of the given item in the
bag. Implement the Counting Bag ADT and defend your selection of data
structure.
"""

class CountingBag:
    """
    Initialize an empty Counting Bag.

    This method initializes an instance of the CountingBag class with an empty dictionary.
    The dictionary, named 'items', will store the items in the bag as keys and their counts as values.

    Parameters:
    None

    Returns:
    None
    """
    def __init__(self):
        self.items = {}

    def add(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def remove(self, item):
        if item in self.items:
            if self.items[item] > 1:
                self.items[item] -= 1
            else:
                del self.items[item]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return sum(self.items.values())

    def num_of(self, item):
        return self.items.get(item, 0)

    def __str__(self):
        return str(self.items)
    

if __name__ == '__main__':
    # Example 1: Basic usage
    bag = CountingBag()
    bag.add("apple")
    bag.add("banana")
    bag.add("apple")
    print("Example 1: Basic usage")
    print("Bag contents:", bag)
    print("Number of 'apple's:", bag.num_of("apple"))
    print("Number of 'banana's:", bag.num_of("banana"))
    print("Number of 'orange's:", bag.num_of("orange"))
    print()

    # Example 2: Removing items
    bag = CountingBag()
    bag.add("apple")
    bag.add("apple")
    bag.add("banana")
    print("Example 2: Removing items")
    print("Initial bag contents:", bag)
    bag.remove("apple")
    print("After removing one 'apple':", bag)
    bag.remove("apple")
    print("After removing another 'apple':", bag)
    bag.remove("apple")
    print("After removing yet another 'apple':", bag)
    print()

    # Example 3: Checking emptiness and size
    bag = CountingBag()
    print("Example 3: Checking emptiness and size")
    print("Is the bag empty?", bag.is_empty())
    print("Bag size:", bag.size())
    bag.add("apple")
    print("Is the bag empty after adding 'apple'?", bag.is_empty())
    print("Bag size after adding 'apple':", bag.size())
    bag.add("banana")
    print("Bag size after adding 'banana':", bag.size())
    print()

    # Example 4: Adding multiple items
    bag = CountingBag()
    bag.add("apple")
    bag.add("apple")
    bag.add("banana")
    bag.add("banana")
    bag.add("banana")
    print("Example 4: Adding multiple items")
    print("Bag contents:", bag)
    print("Number of 'apple's:", bag.num_of("apple"))
    print("Number of 'banana's:", bag.num_of("banana"))
    print()