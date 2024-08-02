# GameOfLifeSparse.py
from SparseLifeGrid import SparseLifeGrid

# Define the initial configuration of live cells.
INIT_CONFIG = [(0, 0), (1, 1), (1, 2), (2, 0), (2, 1)]

# Indicate the number of generations.
NUM_GENS = 20

def main():
    # Construct the game grid and configure it.
    grid = SparseLifeGrid()
    grid.configure(INIT_CONFIG)

    # Play the game.
    draw(grid)
    for i in range(NUM_GENS):
        evolve(grid)
        draw(grid)

def evolve(grid):
    # List for storing the live cells of the next generation.
    liveCells = []

    # Iterate over the elements of the grid.
    for row in range(grid.minRange()[0], grid.maxRange()[0] + 1):
        for col in range(grid.minRange()[1], grid.maxRange()[1] + 1):
            # Determine the number of live neighbors for this cell.
            neighbors = grid.numLiveNeighbors(row, col)

            # Add the (row, col) tuple to liveCells if this cell contains a live organism in the next generation.
            if (grid.isLiveCell(row, col) and neighbors == 2) or (neighbors == 3):
                liveCells.append((row, col))

    # Reconfigure the grid using the liveCells coord list.
    grid.configure(liveCells)

def draw(grid):
    # Print a text-based representation of the game grid.
    for row in range(grid.minRange()[0], grid.maxRange()[0] + 1):
        line = ''
        for col in range(grid.minRange()[1], grid.maxRange()[1] + 1):
            if grid.isLiveCell(row, col):
                line += '@ '
            else:
                line += '. '
        print(line.strip())
    print()

if __name__ == '__main__':
    main()