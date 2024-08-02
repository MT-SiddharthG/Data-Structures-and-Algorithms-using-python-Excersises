# Implementation of the Sparse Matrix ADT using a list.
class SparseMatrix :
    # Create a sparse matrix of size numRows x numCols initialized to 0.
    def __init__( self, numRows, numCols ):
        self._numRows = numRows
        self._numCols = numCols
        self._elementList = list()

    # Return the number of rows in the matrix.
    def numRows( self ):
        return self._numRows

    # Return the number of columns in the matrix.
    def numCols( self ):
        return self._numCols

    # Return the value of element (i, j): x[i,j]
    def __getitem__( self, ndxTuple ):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscripts out of range."
        for element in self._elementList:
            if element.row == row and element.col == col:
                return element.value
        return 0


    # Set the value of element (i,j) to the value s: x[i,j] = s
    def __setitem__( self, ndxTuple, scalar ):
        ndx = self._findPosition( ndxTuple[0], ndxTuple[1] )
        if ndx is not None :
            if scalar != 0.0 :
                self._elementList[ndx].value = scalar
            else :
                self._elementList.pop( ndx )
        else :
            if scalar != 0.0 :
                element = _MatrixElement( ndxTuple[0], ndxTuple[1], scalar )
                self._elementList.append( element )

    # Scale the matrix by the given scalar.
    def scaleBy( self, scalar ):
        for element in self._elementList :
            element.value *= scalar

    # The additional dunder methods
    def __add__( self, rhsMatrix ):
        if self.numRows() != rhsMatrix.numRows() or self.numCols() != rhsMatrix.numCols():
            raise MatrixSizeError( "Matrix sizes not compatible for the operation." )
        else:
            newMatrix = SparseMatrix( self.numRows(), self.numCols() )
            for element in self._elementList:
                newMatrix[element.row, element.col] = element.value
            for element in rhsMatrix._elementList:
                newMatrix[element.row, element.col] += element.value
            return newMatrix

    def __sub__( self, rhsMatrix ):
        if self.numRows() != rhsMatrix.numRows() or self.numCols() != rhsMatrix.numCols():
            raise MatrixSizeError( "Matrix sizes not compatible for the operation." )
        else:
            newMatrix = SparseMatrix( self.numRows(), self.numCols() )
            for element in self._elementList:
                newMatrix[element.row, element.col] = element.value
            for element in rhsMatrix._elementList:
                newMatrix[element.row, element.col] -= element.value
            return newMatrix
        
    def __mul__( self, rhsMatrix ):
        if self.numCols() != rhsMatrix.numRows():
            raise MatrixSizeError( "Matrix sizes not compatible for the operation." )
        else:
            newMatrix = SparseMatrix( self.numRows(), rhsMatrix.numCols() )
            for element in self._elementList:
                for element2 in rhsMatrix._elementList:
                    if element.col == element2.row:
                        newMatrix[element.row, element2.col] += element.value * element2.value
            return newMatrix
        
    def __rmul__( self, scalar ):
        newMatrix = SparseMatrix( self.numRows(), self.numCols() )
        for element in self._elementList:
            newMatrix[element.row, element.col] = element.value * scalar
        return newMatrix
    
    def __eq__( self, rhsMatrix ):
        # Check if the sizes of the matrices are equal
        if self.numRows() != rhsMatrix.numRows() or self.numCols() != rhsMatrix.numCols():
            return False
        
        # Compare elements of the matrices
        for element in self._elementList:
            try:
                # Attempt to access the corresponding element in rhsMatrix
                # Note: This assumes __getitem__ is correctly implemented
                rhsValue = rhsMatrix[element.row, element.col]
            except AssertionError:
                # If accessing rhsMatrix raises an assertion error, it means the indices are out of range,
                # which should not happen if both matrices have the same size. So, we return False.
                return False
            
            # Compare the value of the element in self with the value in rhsMatrix
            if element.value != rhsValue:
                return False
        
        # If all elements match and the sizes are the same, the matrices are equal
        return True
        
    def __ne__( self, rhsMatrix ):
        if self.numRows() != rhsMatrix.numRows() or self.numCols() != rhsMatrix.numCols():
            return True
        else:
            for element in self._elementList:
                if element.row != rhsMatrix[element.row, element.col].row or element.col != rhsMatrix[element.row, element.col].col or \
                element.value != rhsMatrix[element.row, element.col].value:
                    return True
            return False
        
    def add( self, rhsMatrix ):
        return self + rhsMatrix
    
    def sub( self, rhsMatrix ):
        return self - rhsMatrix
    
    def multiply( self, rhsMatrix ):
        return self * rhsMatrix

    # Helper method used to find a specific matrix element (row,col) in the list of non-zero entries. None is returned if the element is not found.
    def _findPosition( self, row, col ):
        n = len( self._elementList )
        for i in range( n ) :
            if row == self._elementList[i].row and col == self._elementList[i].col:
                return i
        return None


# Storage class for holding the non-zero matrix elements.
class _MatrixElement:
    def __init__( self, row, col, value ):
        self.row = row
        self.col = col
        self.value = value


# Exception class used for signalling invalid matrix dimensions.
class MatrixSizeError( Exception ):
    def __init__( self, value ):
        self.value = value


def display_matrix(matrix):
    """Displays the matrix."""
    for i in range(matrix.numRows()):
        row = []
        for j in range(matrix.numCols()):
            row.append(matrix[i, j])
        print(row)

if __name__ == "__main__":
    # Create two sparse matrices
    print("Creating two sparse matrices...")
    matrix1 = SparseMatrix(50, 50)
    matrix1[1, 2] = 10
    matrix1[3, 4] = 12
    matrix1[0, 0] = 5

    matrix2 = SparseMatrix(50, 50)
    matrix2[1, 2] = 2
    matrix2[3, 4] = 4
    matrix2[0, 0] = 1

    # Display matrices
    print("Matrix 1:")
    display_matrix(matrix1)
    print("Matrix 2:")
    display_matrix(matrix2)

    # Addition
    try:
        print("\nAdding Matrix 1 and Matrix 2:")
        result_matrix = matrix1.add(matrix2)
        display_matrix(result_matrix)
    except MatrixSizeError as e:
        print(e.value)

    # Subtraction
    try:
        print("\nSubtracting Matrix 2 from Matrix 1:")
        result_matrix = matrix1.sub(matrix2)
        display_matrix(result_matrix)
    except MatrixSizeError as e:
        print(e.value)

    # Multiplication
    try:
        print("\nMultiplying Matrix 1 and Matrix 2:")
        result_matrix = matrix1.multiply(matrix2)
        display_matrix(result_matrix)
    except MatrixSizeError as e:
        print(e.value)

    # Scaling
    print("\nScaling Matrix 1 by 2:")
    matrix1.scaleBy(2)
    display_matrix(matrix1)

    # Comparison
    print("\nComparing Matrix 1 and Matrix 2:")
    if matrix1 == matrix2:
        print("Matrices are equal.")
    else:
        print("Matrices are not equal.")

