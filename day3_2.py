with open('input3', 'r') as f:
   f_content = f.readlines()
grid = [x[:-1] for x in f_content]

nb_lignes = len(grid)
nb_colonnes = len(grid[0])
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
result = 1

for slope in slopes:
    i, j = 0, 0
    step_j, step_i = slope
    count = 0
    while i < nb_lignes:
        if grid[i][j] == "#":
            count += 1
        j, i = (j + step_j) % nb_colonnes, i + step_i
    result *= count

print(result)
