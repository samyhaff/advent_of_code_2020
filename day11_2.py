from copy import copy, deepcopy

with open("input11", "r") as f:
    f_content = f.read()

def voisin(grille, i, j):
    count = 0 
    max_i = len(grille)
    max_j = len(grille[0])

    for k, l in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
        inc_i = k
        inc_j = l
        while True:
            if not (0 <= i + k < max_i and 0 <= j + l < max_j):
                break 
            if grille[i + k][j + l] == "L":
                break 
            if grille[i + k][j + l] == "#":
                count += 1 
                break 
            k += inc_i
            l += inc_j
    return count

def solve():
    grid = f_content.strip().split("\n")
    grid = [list(x) for x in grid]
    old_grid = [["." for j in range(len(grid[0]))] for i in range(len(grid))]
    while old_grid != grid:
        old_grid = deepcopy(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                adjacent = voisin(old_grid, i, j)
                if (old_grid[i][j] == "L") and (adjacent == 0):
                    grid[i][j] = "#"
                elif (old_grid[i][j] == "#") and (adjacent >= 5):
                    grid[i][j] = "L"
    return sum([x.count("#") for x in grid])

print(solve())
