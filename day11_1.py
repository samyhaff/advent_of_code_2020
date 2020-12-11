from copy import copy, deepcopy

with open("input11", "r") as f:
    f_content = f.read()

def voisin(grille, i, j):
    liste = []
    max_i = len(grille) - 1
    max_j = len(grille[0]) - 1
    if i < max_i:
        liste.append(grille[i + 1][j])
    if j < max_j:
        liste.append(grille[i][j + 1])
    if i > 0:
        liste.append(grille[i - 1][j])
    if j > 0:
        liste.append(grille[i][j - 1])
    if (i + 1 <= max_i) and (j + 1 <= max_j):
        liste.append(grille[i + 1][j + 1])
    if (i > 0) and (j > 0):
        liste.append(grille[i - 1][j - 1])
    if (i > 0) and (j < max_j):
        liste.append(grille[i - 1][j + 1])
    if (i + 1 <= max_i) and (j - 1 >= 0):
        liste.append(grille[i + 1][j - 1])
    return liste

def solve():
    grid = f_content.strip().split("\n")
    grid = [list(x) for x in grid]
    old_grid = [["." for j in range(len(grid[0]))] for i in range(len(grid))]
    while old_grid != grid:
        old_grid = deepcopy(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                adjacent = voisin(old_grid, i, j)
                if (old_grid[i][j] == "L") and (adjacent.count("#") == 0):
                    grid[i][j] = "#"
                elif (old_grid[i][j] == "#") and (adjacent.count("#") >= 4):
                    grid[i][j] = "L"
    return sum([x.count("#") for x in grid])

print(solve())
