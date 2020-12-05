with open('input3', 'r') as f:
   f_content = f.readlines()
grid = [x[:-1] for x in f_content]

count = 0
i , j = 0, 0
nb_lignes = len(grid)
nb_colonnes = len(grid[0])

while i < nb_lignes:
    if grid[i][j] == "#":
        count += 1
    j, i = (j + 3) % nb_colonnes, i + 1

print(count)
