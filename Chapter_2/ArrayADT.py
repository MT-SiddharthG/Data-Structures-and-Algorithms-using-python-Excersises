# Implements the Array ADT using array capabilities of the ctypes module.
import ctypes

class Array:
    """
    Represents an array data type with operations such as initialization,
    getting and setting values, clearing the array, and iteration over elements.
    
    Attributes:
        _size (int): The size of the array.
        _elements (ctypes.py_object * size): A ctypes array object holding the actual elements.
    """

    def __init__(self, size):
        """
        Constructs all the necessary attributes for the Array object.

        Args:
            size (int): The number of elements the array will hold.

        Raises:
            AssertionError: If size <= 0.
        """
        assert size > 0, "Array size must be > 0"
        self._size = size

        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()

        # Initialize each element.
        self.clear(None)

    def __len__(self):
        """
        Returns the size of the array.

        Returns:
            int: The size of the array.
        """
        return self._size

    def __getitem__(self, index):
        """
        Gets the contents of the index element.

        Args:
            index (int): The index of the element to get.

        Returns:
            The element at the specified index.

        Raises:
            AssertionError: If index is out of range.
        """
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[ index ]

    def __setitem__(self, index, value):
        """
        Puts the value in the array element at index position.

        Args:
            index (int): The index where the value should be placed.
            value: The value to place in the array.

        Raises:
            AssertionError: If index is out of range.
        """
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[ index ] = value

    def clear(self, value = None):
        """
        Clears the array by setting each element to the given value.

        Args:
            value: The value to set each element to.
        """
        for i in range( len(self) ) :
            self._elements[i] = value

    def __iter__(self):
        """
        Returns the array's iterator for traversing the elements.

        Returns:
            _ArrayIterator: An iterator object for iterating over the array's elements.
        """
        return _ArrayIterator( self._elements )
    
    

class _ArrayIterator:
    """
    An iterator for the Array ADT, allowing traversal over the array's elements.
    """
    def __init__(self, theArray):
        """
        Constructs all the necessary attributes for the _ArrayIterator object.

        Args:
            theArray (Array): The array to iterate over.
        """
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        """
        Makes the object iterable.

        Returns:
            _ArrayIterator: The iterator itself.
        """
        return self

    def __next__(self):
        """
        Returns the next item from the array.

        Returns:
            The next element from the array.

        Raises:
            StopIteration: If there are no more items to return.
        """
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration
        
if __name__ == "__main__":
    a = Array(5)
    print("Array initialized with size:", len(a))
    a[0] = "Hello"
    a[1] = "World"
    a[2] = 9

    print(f"Getting individual values:")
    print(f"Value at index 0 (a[0]): {a[0]}")
    print(f"Value at index 2 (a[2]): {a[2]}")

    print("After setting values:")
    for i, val in enumerate(a):
        print(f"{i}: {val}")

    a.clear()

    print("\nAfter clearing the array:")
    for i, val in enumerate(a):
        print(f"{i}: {val}")
