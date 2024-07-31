# Implement a Map ADT which will work as python dictionary but implemented with list for minimum functionality
# A map is a container for storing a collection of data records in which each record
# is associated with a unique key. The key components must be comparable.
# Map(): Creates a new empty map.
# length (): Returns the number of key/value pairs in the map.
# contains ( key ): Determines if the given key is in the map and returns True
# if the key is found and False otherwise.
# add( key, value ): Adds a new key/value pair to the map if the key is not
# already in the map or replaces the data associated with the key if the key is in
# the map. Returns True if this is a new key and False if the data associated
# with the existing key is replaced.
# remove( key ): Removes the key/value pair for the given key if it is in the
# map and raises an exception otherwise.
# valueOf( key ): Returns the data record associated with the given key. The
# key must exist in the map or an exception is raised.
# iterator (): Creates and returns an iterator that can be used to iterate over
# the keys in the map.

class Map:
    def __init__(self):
        """
        Initialize an empty map.
        """
        self._entryList = list()

    def __len__(self):
        """
        Return the number of key/value pairs in the map.
        
        :return: The size of the map.
        :rtype: int
        """
        return len(self._entryList)

    def __contains__(self, key):
        """
        Determine if the map contains a specific key.
        
        :param key: The key to check for existence in the map.
        :return: True if the key exists in the map, False otherwise.
        :rtype: bool
        """
        ndx = self._findPosition(key)
        return ndx is not None

    def __getitem__(self, key):
        """
        Return the value associated with a given key.
        
        :param key: The key whose associated value is to be returned.
        :return: The value associated with the key.
        :raises KeyError: If the key does not exist in the map.
        """
        return self.valueOf(key)

    def __setitem__(self, key, value):
        """
        Add a new entry to the map or update the value of an existing key.
        
        :param key: The key of the entry to add or update.
        :param value: The value associated with the key.
        """
        self.add(key, value)

    def add(self, key, value):
        """
        Add a new key/value pair to the map. If the key already exists,
        update the value associated with the key.
        
        :param key: The key of the entry to add.
        :param value: The value associated with the key.
        :return: True if a new key was added, False if an existing key was updated.
        :rtype: bool
        """
        ndx = self._findPosition(key)
        if ndx is not None:
            self._entryList[ndx].value = value
            return False
        else:
            entry = _MapEntry(key, value)
            self._entryList.append(entry)
            return True

    def remove(self, key):
        """
        Remove the entry associated with the given key.
        
        :param key: The key of the entry to remove.
        :raises KeyError: If the key does not exist in the map.
        """
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key."
        self._entryList.pop(ndx)

    def valueOf(self, key):
        """
        Return the value associated with a given key.
        
        :param key: The key whose associated value is to be returned.
        :return: The value associated with the key.
        :raises KeyError: If the key does not exist in the map.
        """
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key."
        return self._entryList[ndx].value

    def __iter__(self):
        """
        Return an iterator for traversing the keys in the map.
        
        :return: An iterator for the map's keys.
        :rtype: _MapIterator
        """
        return _MapIterator(self._entryList)

    def _findPosition(self, key):
        """
        Find the index position of a key in the map. Used internally.
        
        :param key: The key to find.
        :return: The index position of the key if found, None otherwise.
        :rtype: int or None
        """
        n = len(self)
        for i in range(n):
            if self._entryList[i].key == key:
                return i
        return None

    def __str__(self):
        """
        Return a string representation of the map in dictionary format.
        
        :return: A string representing the map.
        :rtype: str
        """
        result = "{"
        for i, entry in enumerate(self._entryList):
            result += f"{entry.key}: {entry.value}"
            if i < len(self._entryList) - 1:
                result += ", "
        result += "}"
        return result

    def __repr__(self):
        """
        Return a formal string representation of the map object.
        
        :return: A string representing the map object.
        :rtype: str
        """
        return f"Map{str(self)}"
    
    # Operator methods for addition. Combine both maps
    def __add__( self, other ):
        """
        Combine both maps

        :param other: The map to combine with.
        :type other: Map
        :return: A new map containing the combined entries.
        """
        newMap = Map()
        for entry in self:
            newMap.add( entry.key, entry.value )
        for entry in other:
            newMap.add( entry.key, entry.value )
        return newMap
    

# Iterator class for map.
class _MapIterator :
    def __init__( self, entryList ):
        self._entryList = entryList
        self._curNdx = 0

    def __iter__( self ):
        return self
    
    def __next__( self ):
        if self._curNdx < len( self._entryList ):
            entry = self._entryList[ self._curNdx ]
            self._curNdx += 1
            return entry.key
        else:
            raise StopIteration

# Storage class for holding the key/value pairs.
class _MapEntry :
    def __init__( self, key, value ):
        self.key = key
        self.value = value

# Test code
if __name__ == "__main__":
    # Create a map and add some entries
    m = Map()
    m.add("CS101", 3)
    m.add("CS102", 4)
    m.add("CS103", 5)
    m.add("NT110", 3)

    print("\nInitial Map:")
    print(m)  # Uses __str__ method to display the map like a dictionary

    print("\nMap Representation:")
    print(repr(m))  # Uses __repr__ method for representation

    print("\nNumber of entries:", len(m))

    print("\nKeys:", end="")
    for key in m:
        print(f" {key}", end="")
    print()

    print("\nValues:", end="")
    for key in m:
        print(f" {m[key]}", end="")
    print()

    print("\nRemove an entry (m.remove('CS101'))")
    m.remove("CS101")

    print("\nMap after removal:")
    print(m)  # Display the map again to show the effect of removal

    print("\nNumber of entries after removal:", len(m))
    
