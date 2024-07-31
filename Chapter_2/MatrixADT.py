# Create Matrix ADT using Array2dADT with following operations
# A matrix is a collection of scalar values arranged in rows and columns as a rectangular grid of a fixed size. The elements of the matrix can be accessed by specifying
# a given row and column index with indices starting at 0.

#  Matrix( rows, ncols ): Creates a new matrix containing nrows and ncols with each element initialized to 0.

#  numRows(): Returns the number of rows in the matrix.

#  numCols(): Returns the number of columns in the matrix.

#  getitem ( row, col ): Returns the value stored in the given matrix element. Both row and col must be within the valid range.

#  setitem ( row, col, scalar ): Sets the matrix element at the given row and col to scalar. The element indices must be within the valid range.

#  scaleBy( scalar ): Multiplies each element of the matrix by the given scalar value. The matrix is modified by this operation.

#  transpose(): Returns a new matrix that is the transpose of this matrix.

#  add ( rhsMatrix ): Creates and returns a new matrix that is the result of adding this matrix to the given rhsMatrix. The size of the two matrices must
# be the same.

#  subtract ( rhsMatrix ): The same as the add() operation but subtracts the two matrices.

#  multiply ( rhsMatrix ): Creates and returns a new matrix that is the result of multiplying this matrix to the given rhsMatrix. The two matrices must be
# of appropriate sizes as defined for matrix multiplication.

from Array2DADT import Array2D

class Matrix:
    """
    Implements a matrix with basic operations such as addition, subtraction,
    multiplication, scaling, and transposition.

    Attributes:
        _theGrid (Array2D): Stores the matrix elements.
    """
    def __init__(self, numRows, numCols):
        """Initializes a matrix with the given number of rows and columns from instance of Array2D."""
        self._theGrid = Array2D(numRows, numCols)
        self._theGrid.clear(0)

    def numRows(self):
        """Returns the number of rows in the matrix."""
        return self._theGrid.numRows()
    
    def numCols(self):
        """Returns the number of columns in the matrix."""
        return self._theGrid.numCols()
    
    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0], ndxTuple[1]]
    
    def __setitem__(self, ndxTuple, scalar):
        self._theGrid[ndxTuple[0], ndxTuple[1]] = scalar

    def __add__(self, rhsMatrix):
        return self.add(rhsMatrix)
    
    def __sub__(self, rhsMatrix):
        return self.subtract(rhsMatrix)

    def __mul__(self, rhsMatrix):
        return self.multiply(rhsMatrix)
    
    def __rmul__(self, scalar):
        newMatrix = Matrix(self.numRows(), self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r, c] * scalar
        return newMatrix
    
    def __str__(self):
        result = ""
        max_row_length = max(len(str(self[r, c])) for r in range(self.numRows()) for c in range(self.numCols()))
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                result += str(self[r, c]).rjust(max_row_length)
                if c < self.numCols() - 1:
                    result += " | "
                else:
                    result += "\n"
            if r < self.numRows() - 1:
                result += ""
        return result
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, rhsMatrix):
        if self.numRows() != rhsMatrix.numRows() or self.numCols() != rhsMatrix.numCols():
            return False
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                if self[r, c] != rhsMatrix[r, c]:
                    return False
        return True
    
    def __ne__(self, rhsMatrix):
        return not self == rhsMatrix

    def scaleBy(self, scalar):
        """
        Scales all elements of the matrix by the given scalar.
        """
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] *= scalar

    def transpose(self):
        """
        Returns a new matrix that is the transpose of this matrix.
        """
        newMatrix = Matrix(self.numCols(), self.numRows())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[c, r] = self[r, c]
        return newMatrix
    
    def add(self, rhsMatrix):
        """
        Adds the current matrix to another matrix of the same size.
        Returns a new matrix.
        """
        assert rhsMatrix.numRows() == self.numRows() and rhsMatrix.numCols() == self.numCols(), \
               "Matrices must be of the same size."
        newMatrix = Matrix(self.numRows(), self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r, c] + rhsMatrix[r, c]

        return newMatrix
    
    def subtract(self, rhsMatrix):
        """
        Subtracts another matrix of the same size from the current matrix.
        Returns a new matrix.
        """
        assert rhsMatrix.numRows() == self.numRows() and rhsMatrix.numCols() == self.numCols(), \
               "Matrices must be of the same size."
        newMatrix = Matrix(self.numRows(), self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r, c] - rhsMatrix[r, c]

        return newMatrix
    
    def multiply(self, rhsMatrix):
        """
        Multiplies the current matrix with another matrix.
        Returns a new matrix.
        """
        assert self.numCols() == rhsMatrix.numRows(), "Matrix dimensions incompatible for multiplication."
        newMatrix = Matrix(self.numRows(), rhsMatrix.numCols())
        for r in range(self.numRows()):
            for c in range(rhsMatrix.numCols()):
                for i in range(self.numCols()):
                    newMatrix[r, c] += self[r, i] * rhsMatrix[i, c]
        return newMatrix
    
    
if __name__ == "__main__":
    # Creating and initializing matrices
    m1 = Matrix(2, 3)
    m1[0, 0] = 1
    m1[0, 1] = 2
    m1[0, 2] = 3
    m1[1, 0] = 4
    m1[1, 1] = 5
    m1[1, 2] = 6
    
    m2 = Matrix(2, 3)
    m2[0, 0] = 1
    m2[0, 1] = 2
    m2[0, 2] = 3
    m2[1, 0] = 4
    m2[1, 1] = 5
    m2[1, 2] = 6

    m3 = Matrix(3, 2)
    m3[0, 0] = 7
    m3[0, 1] = 8
    m3[1, 0] = 9
    m3[1, 1] = 10
    m3[2, 0] = 11
    m3[2, 1] = 12

    # Printing matrices
    print("Matrix 1:")
    print(m1)
    print("\nMatrix 2:")
    print(m2)

    # Addition
    print("\nAddition:")
    print("Matrix 1 + Matrix 2")
    print(m1.add(m2))

    # Subtraction
    print("\nSubtraction:")
    print("Matrix 2 - Matrix 1")
    print(m2.subtract(m1))

    # Multiplication
    print("\nMultiplication:")
    print("Matrix1.multiply(Matrix3)")
    print(m1.multiply(m3))
    print("Matrix2*Matrix3")
    print(m2*m3)

    # Equality Check
    print("\nEquality Check:")
    print("Matrix 1 == Matrix 2")
    print(m1 == m2)
    print("Matrix 1 == Matrix 1")
    print(m1 == m1)
    print("Matrix 1 != Matrix 2")
    print(m1 != m2)
    print("Matrix 1 != Matrix 1")
    print(m1 != m1)

    # Scale by
    print("\nOriginal Matrix:")
    print(m1)
    scaleFactor = 2
    m1.scaleBy(scaleFactor)
    print(f"\nScaled Matrix by {scaleFactor}:")
    print(m1)

    # Transpose
    print("\nTranspose:")
    print("Matrix 1:")
    print(m1)
    print("Matrix 1 Transpose:")
    print(m1.transpose())


    # # Determinant
    # print("\nDeterminant:")
    # print("Matrix 1:")
    # print(m1)
    # print("Determinant:")
    # print(m1.determinant())
    
    # # Inverse
    # print("\nInverse:")
    # print("Matrix 1:")
    # print(m1)
    # print("Inverse:")
    # print(m1.inverse())

    # # Trace
    # print("\nTrace:")
    # print("Matrix 1:")
    # print(m1)
    # print("Trace:")
    # print(m1.trace())

