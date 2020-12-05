with open('input', 'r') as f:
    f_content = f.readlines()

entries = [int(c) for c in f_content]

for i in range(len(entries)):
    for j in range (i + 1, len(entries)):
        if entries[i] + entries[j] == 2020:
            result = entries[i] * entries[j]
            break

print(result)
