'''Generation with Recursive backtracker'''
import pygame
import maze_objects
import saving_maze
from maze_const import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("generation")
clock = pygame.time.Clock()

grid = [maze_objects.Cell(j, i, TILE, screen) for i in range(rows) for j in range(cols)]
stack = []
def main():
    current_cell = grid[0]
    RUN = True
    while RUN:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
        screen.fill(C4)
        [cell.draw() for cell in grid]
        
        current_cell.visited = True
        current_cell.draw_current_cell()
            
        next_cell = current_cell.check_neighbors(grid)
        if next_cell:
            stack.append(current_cell)
            current_cell.remove_walls(next_cell)
            current_cell = next_cell
        elif stack:
            current_cell = stack.pop()
            
        # Обновление дисплея
        pygame.display.flip()
        
    saving_maze.save(grid)
    pygame.quit()

if __name__ == "__main__":
    main()