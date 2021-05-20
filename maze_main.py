import maze_generation
import maze_solution
from maze_const import *

try:
    with open("saved_maze.txt") as file:
        maze = file.read().split()
except FileNotFoundError:
    maze_generation.main()
    with open("saved_maze.txt") as file:
        maze = file.read().split()

k=0
for cell in maze_generation.grid:
    cell.walls = maze[k]
    k+=1

maze_solution.solve(maze_generation.grid)




