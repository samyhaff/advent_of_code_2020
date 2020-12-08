with open("input6", "r") as f:
    f_content = f.read().strip()

f_content = f_content.split("\n\n")
groups = [group.replace('\n', '') for group in f_content]

count = 0
for group in groups:
    count += len(set(group))
print(count)
