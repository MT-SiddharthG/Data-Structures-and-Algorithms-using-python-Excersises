# Program for playing the game of Life.
from LifeGrid import LifeGrid

# Define the initial configuration of live cells.
INIT_CONFIG = [ (0,0), (1,1), (1,2), (2,0), (2,1) ]

# Set the size of the grid.
GRID_WIDTH = 10
GRID_HEIGHT = 10

# Indicate the number of generations.
NUM_GENS = 20

def main():
    # Construct the game grid and configure it.
    grid = LifeGrid( GRID_WIDTH, GRID_HEIGHT )
    grid.configure( INIT_CONFIG )

    # Play the game.
    draw( grid )
    for i in range( NUM_GENS ):
        evolve( grid )
        draw( grid )

# Generates the next generation of organisms.
def evolve( grid ):
    # List for storing the live cells of the next generation.
    liveCells = list()

    # Iterate over the elements of the grid.
    for i in range( grid.numRows() ) :
        for j in range( grid.numCols() ) :
        # Determine the number of live neighbors for this cell.
            neighbors = grid.numLiveNeighbors( i, j )

            # Add the (i,j) tuple to liveCells if this cell contains a live organism in the next generation.
            if (grid.isLiveCell( i, j ) and neighbors == 2) or (neighbors == 3 ) :
                liveCells.append( (i, j) )

    # Reconfigure the grid using the liveCells coord list.
    grid.configure( liveCells )

# Prints a text-based representation of the game grid.
def draw( grid ):
    for i in range(grid.numRows()):
        row = ""
        for j in range(grid.numCols()):
            if grid.isLiveCell(i, j):
                row += "@ "
            else:
                row += ". "
        print(row.strip())
    print()

# Executes the main routine.
main()