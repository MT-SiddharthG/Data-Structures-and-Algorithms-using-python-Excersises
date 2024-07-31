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

from ..Chapter_2.ArrayADT import Array

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

        # Create the 1-D array to store the elements.
        self._elements = Array( size )
        # Create a 1-D array to store the equation factors.
        self._factors = Array( len(dimensions) )
        self._computeFactors()

    # Returns the number of dimensions in the array.
    def numDims( self ):
        return len(self._dims)

    # Returns the length of the given dimension.
    def length( self, dim ):
        assert dim >= 1 and dim < len(self._dims),"Dimension component out of range."
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
        pass