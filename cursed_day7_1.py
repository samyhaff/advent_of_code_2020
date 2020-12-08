with open("input7", "r") as f:
    f_content = f.read()

rules = f_content.strip().split("\n")

bags = []
for rule in rules:
    words = rule.split(" ")
    container = " ".join(words[:2])
    if "no" in words:
        contained = []
    else:
        contained = " ".join(words[4:]).split(",")
        contained = [bag.strip().split(" ") for bag in contained]
        contained = [" ".join(bag[1:3]) for bag in contained]
    bags.append([container, contained])

def solve(bag):
    l = []
    for container, contained in bags:
        if bag in contained:
            l.append(container)
    for x in l:
        l += solve(x)
    return l

result = solve("shiny gold")
print(len(set(result)))
