import pygame
from maze_const import *

def solve(maze):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("solution")
    clock = pygame.time.Clock()

    current_cell = maze[0]
    start_cell = current_cell
    final_cell = maze[-1]

    stack = []
    RUN = True
    while RUN:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        screen.fill(C3)
        pygame.draw.rect(screen, C6, final_cell.rect)
        [cell.draw() for cell in maze]
        current_cell.draw_current_cell()
            
        next_cell = current_cell.solution_check_neighbors(maze)
        if next_cell:
            stack.append(current_cell)
            current_cell.first_solution_visit = True
            current_cell = next_cell
        elif stack:
            current_cell.second_solution_visit = True
            current_cell = stack.pop()

        pygame.display.flip()

        if current_cell is final_cell:
            print("SUCCESS!")
            WAIT = True
            while WAIT:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        WAIT = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETUTN:
                            WAIT = False
            RUN = False
            
    pygame.quit()
