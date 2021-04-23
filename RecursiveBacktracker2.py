import random
import pygame

WIDTH = 1002
HEIGHT = 602
TILE = 10
FPS = 240
cols, rows = WIDTH // TILE, HEIGHT // TILE

# Colors rgb
C1 = (142, 107, 115)
C2 = (215, 221, 234)
C3 = (148, 158, 187)
C4 = (43, 44, 62)
C5 = (19, 19, 23)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Cell(pygame.sprite.Sprite):
    
    def __init__(self, x, y, type):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.type = type
        self.rect = pygame.Rect(self.x * TILE - TILE//2, self.y * TILE  - TILE//2, TILE, TILE)
        self.visited = False

    def check_cell(self, x, y):
        if x < 0 or x > cols-1 or y < 0 or y > rows-1:
            return False
        return grid[x + cols*y]

    def check_neighbors(self):
        neighbors = []
        top_cell = self.check_cell(self.x, self.y-2)
        right_cell = self.check_cell(self.x+2, self.y)
        bottom_cell = self.check_cell(self.x, self.y+2)
        left_cell = self.check_cell(self.x-2, self.y)
        if top_cell and not top_cell.visited:
            neighbors.append(top_cell)
        if right_cell and not right_cell.visited:
            neighbors.append(right_cell)
        if bottom_cell and not bottom_cell.visited:
            neighbors.append(bottom_cell)
        if left_cell and not left_cell.visited:
            neighbors.append(left_cell)
        return random.choice(neighbors) if neighbors else False

    def remove_walls(self, next):
        pass
        dx = self.x - next.x
        dy = self.y - next.y
        if dy == 2:
            mid_cell = self.check_cell(self.x, self.y-1)
            mid_cell.type = "cell"
            mid_cell.visited = True
        elif dy == -2:
            mid_cell = self.check_cell(self.x, self.y+1)
            mid_cell.type = "cell"
            mid_cell.visited = True
        if dx == 2:
            mid_cell = self.check_cell(self.x-1, self.y)
            mid_cell.type = "cell"
            mid_cell.visited = True
        elif dx == -2:
            mid_cell = self.check_cell(self.x+1, self.y)
            mid_cell.type = "cell"
            mid_cell.visited = True

    def draw_current_cell(self):
        pygame.draw.rect(screen, C1, self.rect)

    def draw(self):
        x = self.x * TILE - TILE//2
        y = self.y * TILE - TILE//2
        if self.type == "cell":
            pygame.draw.rect(screen, C4, self.rect)
            if self.visited:
                pygame.draw.rect(screen, C3, self.rect)

def find_start_cell():
    for cell in grid:
        if cell.type == "cell":
            return cell

grid = [Cell(j, i, "cell") if i%2 != 0 and j%2 != 0 and 
                    j-1 < cols and i-1 < rows else Cell(j, i, "wall") for i in range(rows) for j in range(cols)]
current_cell = find_start_cell()
stack = []

RUN = True
while RUN:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

    screen.fill(C5)
    [cell.draw() for cell in grid if cell.type == "cell"]
    current_cell.visited = True
    current_cell.draw_current_cell()
    
    next_cell = current_cell.check_neighbors()
    if next_cell:
        stack.append(current_cell)
        current_cell.remove_walls(next_cell)
        current_cell = next_cell
    elif stack:
        current_cell = stack.pop()


    
# Обновление дисплея
    pygame.display.flip()

pygame.quit()
