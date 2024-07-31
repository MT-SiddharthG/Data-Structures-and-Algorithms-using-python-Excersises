# A life grid is used to represent and store the area in the game of Life that contains organisms. The grid contains a rectangular grouping of cells
# of a finite size divided into rows and columns. The individual cells, which can be alive or dead, are referenced by row and column indices, both of which start at zero.

# LifeGrid( nrows, ncols ): Creates a new game grid consisting of nrows and ncols. All cells in the grid are set to dead.

# numRows(): Returns the number rows in the grid.

# numCols(): Returns the number of columns in the grid.

# configure( coordList ): Configures the grid for evolving the next generation. The coordList argument is a sequence of 2-tuples with each tuple
# representing the coordinates (r, c) of the cells to be set as alive. All remaining cells are cleared or set to dead.

# clearCell( row, col ): Clears the individual cell (row, col) and sets it to dead. The cell indices must be within the valid range of the grid.

# setCell( row, col ): Sets the indicated cell (row, col) to be alive. The cell indices must be within the valid range of the grid.

# isLiveCell( row,col ): Returns a boolean value indicating if the given cell (row, col) contains a live organism. The cell indices must be within the valid
# range of the grid.

# numLiveNeighbors( row, col ): Returns the number of live neighbors for the given cell (row, col). The neighbors of a cell include all of the cells immediately
# surrounding it in all directions. For the cells along the border of the grid, the neighbors that fall outside the grid are assumed to be dead. The cell indices
# must be within the valid range of the grid.

from Array2DADT import Array2D

class LifeGrid :
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    # Creates the game grid and initializes the cells to dead.
    def __init__( self, numRows, numCols ):
        """
        Creates the game grid and initializes the cells to dead.

        :param numRows: the number of rows.
        :param numCols: the number of columns.
        """
        # Allocate the 2-D array for the grid.
        self._grid = Array2D( numRows, numCols )
        # Clear the grid and set all cells to dead.
        self.configure( list() )

    # Returns the number of rows in the grid.
    def numRows( self ):
        """
        Returns the number of rows in the grid.

        :return: the number of rows.
        """
        return self._grid.numRows()

    # Returns the number of columns in the grid.
    def numCols( self ):
        """
        Returns the number of columns in the grid.

        :return: the number of columns.
        """
        return self._grid.numCols()

    # Configures the grid to contain the given live cells.
    def configure( self, coordList ):
        """
        Configures the grid to contain the given live cells.
        The list is a list of tuples, each tuple being (row, col) for a cell that is alive.
        The list is not validated, so it must be within the grid boundaries.

        :param coordList: the list of coordinates for cells that are alive (min=0, max=numRows-1).
        """
        # Clear the game grid.
        for i in range( self.numRows() ):
            for j in range( self.numCols() ):
                self.clearCell( i, j )

    # Set the indicated cells to be alive.
        for coord in coordList :
            self.setCell( coord[0], coord[1] )

    # Does the indicated cell contain a live organism?
    def isLiveCell( self, row, col ):
        """
        Does the indicated cell contain a live organism?

        :param row: the row of the cell.
        :param col: the column of the cell.
        :return: True if the cell is alive, False otherwise.
        """
        return self._grid[row, col] == LifeGrid.LIVE_CELL

    # Clears the indicated cell by setting it to dead.
    def clearCell( self, row, col ):
        """
        Clears the indicated cell by setting it to dead.

        :param row: the row of the cell.
        :param col: the column of the cell.
        """
        self._grid[row, col] = LifeGrid.DEAD_CELL

    # Sets the indicated cell to be alive.
    def setCell( self, row, col ):
        """
        Sets the indicated cell to be alive.

        :param row: the row of the cell.
        :param col: the column of the cell.
        """
        self._grid[row, col] = LifeGrid.LIVE_CELL

    # Returns the number of live neighbors for the given cell.
    def numLiveNeighbors( self, row, col ):
        """
        Returns the number of live neighbors for the given cell.

        :param row: the row of the cell.
        :param col: the column of the cell.
        :return: the number of live neighbors.
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        count = 0
        for direction in directions:
            newRow, newCol = row + direction[0], col + direction[1]
            if newRow >= 0 and newRow < self.numRows() and newCol >= 0 and newCol < self.numCols():
                if self._grid[newRow, newCol] == LifeGrid.LIVE_CELL:
                    count += 1
        return count