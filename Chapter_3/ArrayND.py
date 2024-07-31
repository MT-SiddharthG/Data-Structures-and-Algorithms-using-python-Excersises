# A multi-dimensional array consists of a collection of elements organized into multiple dimensions. 
# Individual elements are referenced by specifying an n-tuple or a subscript of multiple components, (i1, i2, . . . in), one for each dimension of the
# array. All indices of the n-tuple start at zero.

# MultiArray( d1, d2, . . . dn ): Creates a multi-dimensional array of elements organized into n-dimensions with each element initially set to None. The number
# of dimensions, which is specified by the number of arguments, must be greater than 1. The individual arguments, all of which must be greater than zero,
# indicate the lengths of the corresponding array dimensions. The dimensions are specified from highest to lowest, where d1 is the highest possible dimension
# and dn is the lowest.

# dims(): Returns the number of dimensions in the multi-dimensional array. 

# length( dim ): Returns the length of the given array dimension. The individual dimensions are numbered starting from 1, where 1 represents the first, or
# highest, dimension possible in the array. Thus, in an array with three dimensions, 1 indicates the number of tables in the box, 2 is the number of rows,
# and 3 is the number of columns.

# clear( value ): Clears the array by setting each element to the given value.

# getitem ( i1, i2, . . . in ): Returns the value stored in the array at the element position indicated by the n-tuple (i1, i2, . . . in). All of the specified indices
# must be given and they must be within the valid range of the corresponding array dimensions. Accessed using the element operator: y = x[ 1, 2 ].

# setitem ( i1, i2, . . . in, value ): Modifies the contents of the specified array element to contain the given value. The element is specified by the n-tuple
# (i1, i2, . . . in). All of the subscript components must be given and they must be within the valid range of the corresponding array dimensions. Accessed
# using the element operator: x[ 1, 2 ] = y.

# iter(): Returns an iterator for the array.

from Chapter_2.ArrayADT import Array

# Implementation of the MultiArray ADT using a 1-D array.
class MultiArray :
    # Creates a multi-dimensional array.
    def __init__( self, *dimensions ):
        assert len(dimensions) > 1, "The array must have 2 or more dimensions."

        # The variable argument tuple contains the dim sizes.
        self._dims = dimensions

        # Compute the total number of elements in the array.
        size = 1
        for d in dimensions :
            assert d > 0, "Dimensions must be > 0."
            size *= d
        print(self._dims)
        # Create the 1-D array to store the elements.
        self._elements = Array( size )
        # Create a 1-D array to store the equation factors.
        self._factors = Array( len(dimensions) )

        for i in range(len(self._factors)):
            self._factors[i] = 1

        self._computeFactors()

    # Returns the number of dimensions in the array.
    def numDims( self ):
        return len(self._dims)

    # Returns the length of the given dimension.
    def length( self, dim ):
        assert dim >= 0 and dim < len(self._dims),"Dimension component out of range."
        return self._dims[dim - 1]

    # Clears the array by setting all elements to the given value.
    def clear( self, value ):
        self._elements.clear( value )

    # Returns the contents of element (i_1, i_2, ..., i_n).
    def __getitem__( self, ndxTuple ):
        assert len(ndxTuple) == self.numDims(), "Invalid # of array subscripts."
        index = self._computeIndex( ndxTuple )
        assert index is not None, "Array subscript out of range."
        return self._elements[index]

    # Sets the contents of element (i_1, i_2, ..., i_n).
    def __setitem__( self, ndxTuple, value ):
        assert len(ndxTuple) == self.numDims(), "Invalid # of array subscripts."
        index = self._computeIndex( ndxTuple )
        assert index is not None, "Array subscript out of range."
        self._elements[index] = value

    # Computes the 1-D array offset for element (i_1, i_2, ... i_n) using the equation i_1 * f_1 + i_2 * f_2 + ... + i_n * f_n
    def _computeIndex( self, idx ):
        offset = 0
        for j in range( len(idx) ):
        # Make sure the index components are within the legal range.
            if idx[j] < 0 or idx[j] >= self._dims[j] :
                return None
        else :
            offset += idx[j] * self._factors[j]
        return offset

    # Computes the factor values used in the index equation.
    def _computeFactors( self ):
        for j in range( len(self._dims) - 1 ) :
            self._factors[j + 1] = self._dims[j] * self._factors[j]
            self._factors[0] = 1
    
    # # Returns the array's string representation.
    # def __str__( self ):
    #     return str(self._elements.__str__())
    
    # # Returns the array's string representation.
    # def __repr__( self ):
    #     return repr(self._elements)
    
# Test program
if __name__ == '__main__':
    # Example 1: Creating a 2D MultiArray (3 rows x 4 columns)
    print("Example 1: Creating a 2D MultiArray (3 rows x 4 columns)")
    ma_2d = MultiArray(3, 4)
    print(f"Dimensions: {ma_2d.numDims()}, Length of dimension 1: {ma_2d.length(0)}, Length of dimension 2: {ma_2d.length(1)}")
    
    # Setting values in the 2D MultiArray
    ma_2d[0, 1] = 10
    ma_2d[1, 2] = 20
    ma_2d[2, 3] = 30
    
    # Getting values from the 2D MultiArray
    print(f"Value at position (0, 1): {ma_2d[0, 1]}")
    print(f"Value at position (1, 2): {ma_2d[1, 2]}")
    print(f"Value at position (2, 3): {ma_2d[2, 3]}")
    print("--------------------------------------------------\n")

    # Example 2: Creating a 3D MultiArray (2 x 3 x 4)
    print("Example 2: Creating a 3D MultiArray (2 x 3 x 4)")
    ma_3d = MultiArray(2, 3, 4)
    print(f"Dimensions: {ma_3d.numDims()}, Length of dimension 1: {ma_3d.length(0)}, Length of dimension 2: {ma_3d.length(1)}, Length of dimension 3: {ma_3d.length(2)}")
    
    # Setting values in the 3D MultiArray
    ma_3d[0, 1, 2] = 100
    ma_3d[1, 2, 3] = 200
    ma_3d[0, 2, 3] = 300
    
    # Getting values from the 3D MultiArray
    print(f"Value at position (0, 1, 2): {ma_3d[0, 1, 2]}")
    print(f"Value at position (1, 2, 3): {ma_3d[1, 2, 3]}")
    print(f"Value at position (0, 2, 3): {ma_3d[0, 2, 3]}")
    print("--------------------------------------------------\n")

    # Example 3: Clearing a MultiArray
    print("Example 3: Clearing a MultiArray")
    ma_2d.clear(0)  # Setting all elements to 0
    print(f"After clearing, value at position (0, 1): {ma_2d[0, 1]}")
    print("--------------------------------------------------\n")
    
