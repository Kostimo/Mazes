import random
import pygame
from maze_const import *

class Cell(pygame.sprite.Sprite):
    
    def __init__(self, x, y, TILE, surface, walls=None):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.tile = TILE
        self.surface = surface
        self.rect = pygame.Rect(self.x * self.tile, self.y * self.tile, self.tile, self.tile)
        self.visited = False
        self.first_solution_visit = False
        self.second_solution_visit = False
        self.walls = {"top": True, "right": True, "bottom": True, "left": True} if walls is None else walls

    def check_cell(self, x, y, grid):
        if x < 0 or x > cols-1 or y < 0 or y > rows-1:
            return False
        return grid[x + cols*y]

    def check_neighbors(self, grid):
        neighbors = []
        top_cell = self.check_cell(self.x, self.y-1, grid)
        right_cell = self.check_cell(self.x+1, self.y, grid)
        bottom_cell = self.check_cell(self.x, self.y+1, grid)
        left_cell = self.check_cell(self.x-1, self.y, grid)
        if top_cell and not top_cell.visited:
            neighbors.append(top_cell)
        if right_cell and not right_cell.visited:
            neighbors.append(right_cell)
        if bottom_cell and not bottom_cell.visited:
            neighbors.append(bottom_cell)
        if left_cell and not left_cell.visited:
            neighbors.append(left_cell)
        return random.choice(neighbors) if neighbors else False

    def solution_check_neighbors(self, grid):
        neighbors = []
        top_cell = self.check_cell(self.x, self.y-1, grid)
        right_cell = self.check_cell(self.x+1, self.y, grid)
        bottom_cell = self.check_cell(self.x, self.y+1, grid)
        left_cell = self.check_cell(self.x-1, self.y, grid)
        if top_cell and not int(self.walls[1]) and not top_cell.first_solution_visit and (
                                                   not top_cell.second_solution_visit):
            neighbors.append(top_cell)
        if right_cell and not int(self.walls[2]) and not right_cell.first_solution_visit and (
                                                     not right_cell.second_solution_visit):
            neighbors.append(right_cell)
        if bottom_cell and not int(self.walls[3]) and not bottom_cell.first_solution_visit and (
                                                      not bottom_cell.second_solution_visit):
            neighbors.append(bottom_cell)
        if left_cell and not int(self.walls[0]) and not left_cell.first_solution_visit and (
                                                    not left_cell.second_solution_visit):
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

    def wall_convesion(self):
        index = ""
        if self.walls["left"]:
            index += "1"
        else:
            index += "0"
        if self.walls["top"]:
            index += "1"
        else:
            index += "0"
        if self.walls["right"]:
            index += "1"
        else:
            index += "0"
        if self.walls["bottom"]:
            index += "1"
        else:
            index += "0"
        return index

    def draw_current_cell(self):
        pygame.draw.rect(self.surface, C1, self.rect)

    def draw(self):
        x = self.x * self.tile
        y = self.y * self.tile
        if self.visited:
            pygame.draw.rect(self.surface, C3, self.rect)
        if self.first_solution_visit:
            pygame.draw.rect(self.surface, C7, self.rect)
        if self.second_solution_visit:
            pygame.draw.rect(self.surface, C4, self.rect)
        if isinstance(self.walls, dict):
            if self.walls["top"]:
                pygame.draw.line(self.surface, C5, (x, y), (x + self.tile, y), 2)
            if self.walls["right"]:
                pygame.draw.line(self.surface, C5, (x + self.tile, y), (x + self.tile, y + self.tile), 2)
            if self.walls["bottom"]:
                pygame.draw.line(self.surface, C5, (x, y + self.tile), (x + self.tile, y + self.tile), 2)
            if self.walls["left"]:
                pygame.draw.line(self.surface, C5, (x, y), (x, y + self.tile), 2)
        elif isinstance(self.walls, str):
            if int(self.walls[0]):
                pygame.draw.line(self.surface, C5, (x, y), (x, y + self.tile), 2)
            if int(self.walls[1]):
                pygame.draw.line(self.surface, C5, (x, y), (x + self.tile, y), 2)
            if int(self.walls[2]):
                pygame.draw.line(self.surface, C5, (x + self.tile, y), (x + self.tile, y + self.tile), 2)
            if int(self.walls[3]):
                pygame.draw.line(self.surface, C5, (x, y + self.tile), (x + self.tile, y + self.tile), 2)