# Implementation of the Set ADT container using a Python list.

class Set:
    """
    Set() creates an empty set instance.
    Set(element, element, ...) creates a set instance with the given elements.
    """
    # Creates an empty set instance or initializes it with elements.
    def __init__(self, *initElements):
        """
        Creates an empty set instance or initializes it with elements.

        Parameters:
            initElements (any): Initial elements to add to the set.
        """
        self._theElements = list()
        if len(initElements) > 0:
            for element in initElements:
                self.add(element)

    # Returns the number of items in the set.
    def __len__(self):
        """
        Returns the number of items in the set.
        """
        return len(self._theElements)

    # Determines if an element is in the set.
    def __contains__(self, element):
        """
        Determines if an element is in the set.

        Parameters:
            element (any): The element to search for.
        Returns:
            (bool): True if the element is in the set, False otherwise.
        """
        return element in self._theElements

    # Adds a new unique element to the set.
    def add(self, element):
        """
        Adds a new unique element to the set.

        Parameters:
            element (any): The element to add.
        Returns:
            (bool): True if the element was added, False otherwise.
        """
        if element not in self:
            self._theElements.append(element)

    # Removes an element from the set.
    def remove(self, element):
        """
        Removes an element from the set.

        Parameters:
            element (any): The element to remove.
        Returns:
            (bool): True if the element was removed, False otherwise.
        """
        assert element in self, "The element must be in the set."
        self._theElements.remove( element )

    # Determines if two sets are equal.
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else :
            return self.isSubsetOf( setB )

    # Determines if this set is a subset of setB.
    def isSubsetOf(self, setB):
        """
        Determines if this set is a subset of setB.

        Parameters:
            setB (Set): The set to compare to.
        Returns:
            (bool): True if this set is a subset of setB, False otherwise.
        """
        for element in self:
            if element not in setB:
                return False
        return True

    # Creates a new set from the union of this set and setB.
    def union(self, setB):
        """
        Creates a new set from the union of this set and setB.

        Parameters:
            setB (Set): The set to union with.
        Returns:
            (Set): The new set.
        """
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

    # Creates a new set from the intersection: self set and setB.
    def intersect(self, setB):
        """
        Creates a new set from the intersection: self set and setB.

        Parameters:
            setB (Set): The set to intersect with.
        Returns:
            (Set): The new set.
        """
        newSet = Set()
        for element in self:
            if element in setB:
                newSet.add(element)
        return newSet

    # Creates a new set from the difference: self set and setB.
    def difference(self, setB):
        """
        Creates a new set from the difference: self set and setB.

        Parameters:
            setB (Set): The set to difference with.
        Returns:
            (Set): The new set.
        """
        newSet = Set()
        for element in self:
            if element not in setB:
                newSet.add(element)
        return newSet

    # Returns an iterator for traversing the list of items.
    def __iter__(self):
        return _SetIterator(self._theElements)
    
    # String representation of the set.
    def __str__(self):
        return "{" + ", ".join(map(str, self._theElements)) + "}"

    # Operator methods for set operations.
    def __add__(self, setB):
        return self.union(setB)

    def __mul__(self, setB):
        return self.intersect(setB)

    def __sub__(self, setB):
        return self.difference(setB)
    
    def __lt__(self, setB):
        return self.isSubsetOf(setB)
    
    def __le__(self, setB):
        return self.isSubsetOf(setB) or self == setB
    
    def __gt__(self, setB):
        return not self.isSubsetOf(setB)
    
    def __ge__(self, setB):
        return not self.isSubsetOf(setB) or self == setB
    


class _SetIterator :
    # An iterator for the Set ADT implemented as a Python list.
    def __init__( self, theList ):
        self._theItems = theList
        self._curItem = 0

    def __iter__( self ):
        return self
    
    def __next__( self ):
        if self._curItem < len( self._theItems ) :
            item = self._theItems[ self._curItem ]
            self._curItem += 1
            return item
        else :
            raise StopIteration
        
if __name__=='__main__':
    s1 = Set()
    print("Set s1 before adding elements:", s1)
    s1.add(1)
    s1.add(2)
    s1.add(3)
    s1.add(4)
    print("Set s1 after adding elements:", s1)

    # Addition of element already present in set
    s1.add(4)
    print("Set s1 after adding element already present (s1.add(4)):", s1)

    # Removal of element present in set
    s1.remove(4)
    print("Set s1 after removing element present (s1.remove(4)):", s1)

    s2 = Set(1,2,3)
    print("Set s2 with elements 1,2,3 in constructor (s2=Set(1,2,3)):", s2)

    s3 = Set(3,4,5)
    print("Set s3 with elements 3,4,5 in constructor (s3=Set(3,4,5)):", s3)

    #union operations
    union_set = s1.union(s3)
    print("\nUnion of s1 and s3 using dot operator (s1.union(s2)): ", union_set)

    # intersection operations
    intersection_set = s1.intersect(s3)
    print("\nIntersection of s1 and s3 using dot operator (s1.intersect(s2)): ", intersection_set)

    # difference operations
    difference_set = s1.difference(s3)
    print("\nDifference of s1 and s3 using dot operator (s1.difference(s2)): ", difference_set)

    # iterator operations
    print("\nIterating over s1 using for loop:")
    for i in s1:
        print("Element:", i)
    
    # membership operations using in
    print("\nChecking if 1 is in s1 using 'in' operator:", 1 in s1)

    # membership operations using not in
    print("\nChecking if 1 is not in s1 using 'not in' operator:", 1 not in s1)

    # union operations using + operator
    union_set = s1 + s2
    print("\nUnion of s1 and s2 using + operator (s1+s2): ", union_set)

    # intersection operations using * operator
    intersection_set = s1 * s2
    print("\nIntersection of s1 and s2 using * operator (s1*s2): ", intersection_set)

    # difference operations using - operator
    difference_set = s1 - s3
    print("\nDifference of s1 and s3 using - operator (s1-s3): ", difference_set)

    # subset operations using <= operator
    print("\nChecking if s1 is a subset of s2 using <= operator (s1<=s2):", s1 <= s3)

    # superset operations using >= operator
    print("\nChecking if s1 is a superset of s2 using >= operator (s1>=s2):", s1 >= s3)


