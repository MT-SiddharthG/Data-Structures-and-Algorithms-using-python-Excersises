# The game of Life is defined for an infinite-sized grid. In Chapter_2, we defined the Life Grid ADT to use a fixed-size grid in which the user specified the width
# and height of the grid. This was sufficient as an illustration of the use of a 2-D array for the implementation of the game of Life. But a full implementation
# should allow for an infinite-sized grid. Implement the Sparse Life Grid ADT using an approach similar to the one used to implement the sparse matrix.

# SparseLifeGrid(): Creates a new infinite-sized game grid. All cells in
# the grid are initially set to dead.

# minRange(): Returns a 2-tuple (minrow, mincol) that contains the minimum row index and the minimum column index that is currently occupied
# by a live cell.

# maxRange(): Returns a 2-tuple (maxrow, maxcol) that contains the maximum row index and the maximum column index that is currently occupied
# by a live cell.

# configure( coordList ): Configures the grid for evolving the first generation. The coordList argument is a sequence of 2-tuples with each
# tuple representing the coordinates (r, c) of the cells to be set as alive. All remaining cells are cleared or set to dead.

# clearCell( row, col ): Clears the individual cell (row, col) and sets it to dead. The cell indices must be within the valid range of the grid.

# setCell( row, col ): Sets the indicated cell (row, col) to be alive. The cell indices must be within the valid range of the grid.
# 
# isLiveCell( row,col ): Returns a boolean value indicating if the given cell (row, col) contains a live organism. The cell indices must be within
# the valid range of the grid.

# numLiveNeighbors( row, col ): Returns the number of live neighbors for the given cell (row, col). The neighbors of a cell include all of the cells immediately surrounding it in all directions. For the cells along the border
# of the grid, the neighbors that fall outside the grid are assumed to be dead. The cell indices must be within the valid range of the grid.

class SparseLifeGrid:
    """
    Implements the Game of Life grid using a sparse matrix approach.
    
    Attributes:
        _grid (dict): A dictionary representing the grid, where keys are tuples (row, col) of live cells.
        _minrow (int): The minimum row index currently occupied by a live cell.
        _maxrow (int): The maximum row index currently occupied by a live cell.
        _mincol (int): The minimum column index currently occupied by a live cell.
        _maxcol (int): The maximum column index currently occupied by a live cell.
    """
    
    def __init__(self):
        self._grid = {}
        self._minrow = self._maxrow = None
        self._mincol = self._maxcol = None
    
    def minRange(self):
        """Returns a 2-tuple (minrow, mincol) that contains the minimum row and column indices currently occupied by a live cell."""
        return (self._minrow, self._mincol)
    
    def maxRange(self):
        """Returns a 2-tuple (maxrow, maxcol) that contains the maximum row and column indices currently occupied by a live cell."""
        return (self._maxrow, self._maxcol)
    
    def configure(self, coordList):
        """
        Configures the grid for evolving the first generation. The coordList argument is a sequence of 2-tuples with each tuple representing the coordinates (row, col) of the cells to be set as alive. All remaining cells are cleared or set to dead.
        
        Args:
            coordList (list): A list of tuples representing the coordinates of live cells.
        """
        self._grid.clear()
        self._minrow = self._maxrow = None
        self._mincol = self._maxcol = None
    
    def minRange(self):
        """Returns a 2-tuple (minrow, mincol) that contains the minimum row and column indices currently occupied by a live cell."""
        return (self._minrow, self._mincol)
    
    def maxRange(self):
        """Returns a 2-tuple (maxrow, maxcol) that contains the maximum row and column indices currently occupied by a live cell."""
        return (self._maxrow, self._maxcol)
    
    def configure(self, coordList):
        """
        Configures the grid for evolving the first generation. The coordList argument is a sequence of 2-tuples with each tuple representing the coordinates (row, col) of the cells to be set as alive. All remaining cells are cleared or set to dead.
        
        Args:
            coordList (list): A list of tuples representing the coordinates of live cells.
        """
        self._grid.clear()
        self._minrow = self._maxrow = None
        self._mincol = self._maxcol = None
        for row, col in coordList:
            self.setCell(row, col)

    def clearCell(self, row, col):
        """Clears the individual cell (row, col) and sets it to dead."""
        try:
            del self._grid[(row, col)]
            if not self._grid:
                self._minrow = self._maxrow = None
                self._mincol = self._maxcol = None
        except KeyError:
            pass

    def setCell(self, row, col):
        """Sets the indicated cell (row, col) to be alive."""
        self._grid[(row, col)] = True
        if self._minrow is None or row < self._minrow:
            self._minrow = row
        if self._maxrow is None or row > self._maxrow:
            self._maxrow = row
        if self._mincol is None or col < self._mincol:
            self._mincol = col
        if self._maxcol is None or col > self._maxcol:
            self._maxcol = col

    def isLiveCell(self, row, col):
        """Returns a boolean value indicating if the given cell (row, col) contains a live organism."""
        return (row, col) in self._grid

    def numLiveNeighbors(self, row, col):
        """
        Returns the number of live neighbors for the given cell (row, col).
        
        Neighbors include all cells immediately surrounding the given cell in all directions.
        """
        return sum(self.isLiveCell(row + dr, col + dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr != 0 or dc != 0))

    def __str__(self):
        """Returns a string representation of the grid."""
        lines = []
        for row in range(self._minrow, self._maxrow + 1):
            line = ''.join('@' if self.isLiveCell(row, col) else '.' for col in range(self._mincol, self._maxcol + 1))
            lines.append(line)
        return '\n'.join(lines)
    
    def __repr__(self):
        return 'Grid(%s)' % repr(self._grid)
    
# Test Code
if __name__ == '__main__':
    grid = SparseLifeGrid()
    initial_config = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2)]
    grid.configure(initial_config)
    print(grid)
    print(f"Live neighbors of (1, 1): {grid.numLiveNeighbors(1, 1)}")
    grid.clearCell(2, 2)
    print(grid)
    print(f"Live neighbors of (1, 1): {grid.numLiveNeighbors(1, 1)}")


    grid = SparseLifeGrid()
    # Adding a glider to the initial configuration
    initial_config = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    grid.configure(initial_config)
    print("Initial Configuration:")
    print(grid)
    
    # Simulating one generation change
    next_generation = []
    for row in range(grid.minRange()[0] - 1, grid.maxRange()[0] + 2):
        for col in range(grid.minRange()[1] - 1, grid.maxRange()[1] + 2):
            live_neighbors = grid.numLiveNeighbors(row, col)
            if (grid.isLiveCell(row, col) and live_neighbors in [2, 3]) or (not grid.isLiveCell(row, col) and live_neighbors == 3):
                next_generation.append((row, col))
    
    # Configure the grid for the next generation
    grid.configure(next_generation)
    print("\nAfter one generation:")
    print(grid)