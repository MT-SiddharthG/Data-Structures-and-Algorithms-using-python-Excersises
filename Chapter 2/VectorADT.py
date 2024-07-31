from ArrayADT import Array

class Vector:
    def __init__(self, capacity=2):
        """
        Initializes a new Vector instance with the specified capacity.
        
        Args:
            capacity (int): The initial capacity of the vector.
        """
        self.array = Array(capacity)
        self.size = 0

    def __len__(self):
        """
        Returns the number of items in the vector.
        
        Returns:
            int: The number of items in the vector.
        """
        return self.size

    def __getitem__(self, index):
        """
        Retrieves the item at the specified index.
        
        Args:
            index (int): The index of the item to retrieve.
            
        Returns:
            The item at the specified index.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.array[index]

    def __setitem__(self, index, value):
        """
        Sets the item at the specified index to the given value.
        
        Args:
            index (int): The index of the item to set.
            value: The value to set the item to.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.array[index] = value

    def append(self, value):
        if self.size == len(self.array):
            self._resize()
        self.array[self.size] = value
        self.size += 1

    def _resize(self):
        if self.size == len(self.array):
            new_capacity = max(1, 2 * self.size)
        elif self.size < len(self.array) * 0.55:
            new_capacity = max(1, len(self.array) // 2)
        else:
            return  # No resizing needed
        new_array = Array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.size == len(self.array):
            self._resize()
        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = value
        self.size += 1
        self._resize()

    def remove(self, index=None):
        """
        Removes the element at the specified index or the last element if no index is specified.
        
        Args:
            index (int, optional): The index of the element to remove. Defaults to None, which removes the last element.
            
        Returns:
            The removed element.
            
        Raises:
            IndexError: If the index is out of range.
        """
        if index is None:
            index = self.size - 1
        
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        removed_element = self.array[index]
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1
        
        # Check if resizing is needed after removal
        self._resize()
        
        return removed_element


    def __str__(self):
        """
        Returns a string representation of the vector.
        
        Returns:
            str: A string representation of the vector.
        """
        return str(self.__repr__())

    def __repr__(self):
        """
        Returns a detailed string representation of the vector.
        
        Returns:
            str: A detailed string representation of the vector.
        """
        elements_str = ', '.join(str(self.array[i]) for i in range(self.size))
        return f"Vector([{elements_str}])"
    

if __name__ == "__main__":
    v = Vector(2)
    print("Initial Vector:")
    print(v)
    print(v.array._size)  
    v.append('a')
    v.append('b')
    v.append('c')
    print("\nAfter appending 'a', 'b', 'c':")
    print(v)  # Output: ['a', 'b', 'c']
    print(v.array._size)

    # Inserting a value at a specific index
    v.insert(1, 'x')
    print("\nAfter inserting 'x' at index 1:")
    print(v)
    print(v.array._size)

    # Removing a value and checking the result
    removed_item = v.remove(2)
    print("\nRemoving the item at index 2 (v.remove(2)):")
    print(f"Removed item: '{removed_item}'")
    print(v)
    print(v.array._size)

    removed_item = v.remove()
    print("\nRemoving the item without parameter removes the last item (v.remove()):")
    print(f"Removed item: '{removed_item}'")
    print(v)
    print(v.array._size)

    # Demonstrating resizing due to capacity increase
    v.append('d')
    print("\nAppending 'd' (causes resizing):")
    print(v)
    print(v.array._size)
