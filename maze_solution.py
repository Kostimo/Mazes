import pygame
import maze_generation

FPS = 10
TILE = maze_generation.TILE
cols, rows = maze_generation.cols, maze_generation.rows
WIDTH, HEIGHT = TILE*cols+2, TILE*rows+2

# Colors rgb
C1 = (142, 107, 115)
C2 = (215, 221, 234)
C3 = (148, 158, 187)
C4 = (43, 44, 62)
C5 = (19, 19, 23)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

with open("saved_maze.txt") as file:
    maze = file.read().split()

grid = maze_generation.grid
k=0
for cell in grid:
    cell.walls = maze[k]
    k+=1

RUN = True
while RUN:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    screen.fill(C3)
    [cell.draw() for cell in grid]

    pygame.display.flip()
pygame.quit()


