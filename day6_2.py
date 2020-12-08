with open("input6", "r") as f:
    f_content = f.read().strip()

f_content = f_content.split("\n\n")
members_count = [group.count("\n") + 1 for group in f_content]
groups = [group.replace('\n', '') for group in f_content]

result = 0
for i in range(len(groups)):
    count = 0
    counts = [0] * 26
    for question in groups[i]:
        counts[ord(question) - 97] += 1
    for question_count in counts:
        if question_count == members_count[i]:
            count += 1
    result += count
print(result)
