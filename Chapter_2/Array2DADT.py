from ArrayADT import Array

# Implementation of the Array2D ADT using an array of arrays.
class Array2D:
    """
    Represents a two-dimensional array with operations such as initialization,
    getting and setting values, clearing the array, and accessing dimensions.
    """
    def __init__(self, numRows, numCols):
        # Create a 1-D array to store an array reference for each row.
        self._theRows = Array( numRows )

        # Create the 1-D arrays for each row of the 2-D array.
        for i in range(numRows):
            self._theRows[i] = Array(numCols)

    # Returns the number of rows in the 2-D array.
    def numRows(self):
        """
        Returns the number of rows in the 2-D array.

        Returns:
            int: Number of rows in the 2-D array.
        """
        return len(self._theRows)

    # Returns the number of columns in the 2-D array.
    def numCols(self):
        """
        Returns the number of columns in the 2-D array.

        Returns:
            int: Number of columns in the 2-D array.
        """
        return len(self._theRows[0])

    # Clears the array by setting every element to the given value.
    def clear(self, value = None):
        """
        Clears the array by setting every element to the given value.

        Args:
            value: Value to set each element to.
        """
        for row in self._theRows:
            row.clear(value)

    # Gets the contents of the element at position [i, j]
    def __getitem__(self, ndxTuple):
        """
        Gets the contents of the element at position [i, j].

        Args:
            ndxTuple (tuple): Tuple containing the row and column indices.

        Returns:
            The element at the specified position [i, j].

        Raises:
            AssertionError: If the indices are out of range.
        """
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscript out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]

    # Sets the contents of the element at position [i,j] to value.
    def __setitem__(self, ndxTuple, value):
        """
        Sets the contents of the element at position [i, j] to value.

        Args:
            ndxTuple (tuple): Tuple containing the row and column indices.
            value: Value to set at the specified position [i, j].

        Raises:
            AssertionError: If the indices are out of range.
        """
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value

if __name__ == "__main__":
    # Example usage of Array2D
    my2DArray = Array2D(3, 4)
    print("Created a 3x4 2D array.")

    print("Setting values: ")
    print('''my2DArray[0][0] = 1\nmy2DArray[1,1] = 2\nmy2DArray[2,2] = 3\nmy2DArray[0,3] = 4''')
    # Setting values
    my2DArray[0,0] = 1
    my2DArray[1,1] = 2
    my2DArray[2,2] = 3
    my2DArray[0,3] = 4

    print("Getting values:")
    for i in range(my2DArray.numRows()):
        for j in range(my2DArray.numCols()):
            print(f"Element at [{i}, {j}]: {my2DArray[i,j]}")

    # Clearing the array
    print("\nClearing the array with value 0: my2DArray.clear(0)")
    my2DArray.clear(0)
    for i in range(my2DArray.numRows()):
        for j in range(my2DArray.numCols()):
            print(f"Element at [{i}, {j}]: {my2DArray[i,j]}")