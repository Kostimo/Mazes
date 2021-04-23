import random
import pygame

WIDTH = 1002
HEIGHT = 602
TILE = 100
FPS = 5
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
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y 
        self.rect = pygame.Rect(self.x * TILE, self.y * TILE, TILE, TILE)
        self.visited = False
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}

    def check_cell(self, x, y):
        if x < 0 or x > cols-1 or y < 0 or y > rows-1:
            return False
        return grid[x + cols*y]

    def check_neighbors(self):
        neighbors = []
        top_cell = self.check_cell(self.x, self.y-1)
        right_cell = self.check_cell(self.x+1, self.y)
        bottom_cell = self.check_cell(self.x, self.y+1)
        left_cell = self.check_cell(self.x-1, self.y)
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
        dx = self.x - next.x
        dy = self.y - next.y
        if dy == 1:
            self.walls["top"] = False
            next.walls["bottom"] = False
        elif dy == -1:
            self.walls["bottom"] = False
            next.walls["top"] = False
        if dx == 1:
            self.walls["left"] = False
            next.walls["right"] = False
        elif dx == -1:
            self.walls["right"] = False
            next.walls["left"] = False

    def draw_current_cell(self):
        pygame.draw.rect(screen, C1, self.rect)

    def draw(self):
        x = self.x * TILE
        y = self.y * TILE
        if self.visited:
            pygame.draw.rect(screen, C3, self.rect)
        if self.walls["top"]:
            pygame.draw.line(screen, C5, (x, y), (x + TILE, y), 2)
        if self.walls["right"]:
            pygame.draw.line(screen, C5, (x + TILE, y), (x + TILE, y + TILE), 2)
        if self.walls["bottom"]:
            pygame.draw.line(screen, C5, (x, y + TILE), (x + TILE, y + TILE), 2)
        if self.walls["left"]:
            pygame.draw.line(screen, C5, (x, y), (x, y + TILE), 2)

grid = [Cell(j, i) for i in range(rows) for j in range(cols)]
current_cell = grid[0]
stack = []

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