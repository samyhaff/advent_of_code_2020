with open('input2', 'r') as f:
    entries = f.readlines()

count = 0 
for entry in entries:
    interval, lettre, password = entry.split(" ")
    i, j = interval.split("-")
    i, j = int(i), int(j)
    lettre = lettre[0]
    if (password[i - 1] == lettre) != (password[j - 1] == lettre):
        count += 1

print(count)
