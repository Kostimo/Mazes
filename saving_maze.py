from maze_const import *
def save(grid):
    # Создание массива, хранящего значения стен каждой клетки лабиринта
    maze = [(cell.wall_convesion()) for cell in grid]

    # Запись значения стен в файл
    with open("saved_maze.txt", "w") as file:
        for i, el in enumerate(maze):
            if (i+1)%cols == 0:
                file.write(str(el) + "\n")
            else:
                file.write(str(el) + " ")