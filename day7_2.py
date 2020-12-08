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
        contained = [" ".join(bag[:3]) for bag in contained]
    bags.append([container, contained])

def solve(bag):
    count = 0
    for container, contained in bags:
        if container == bag:
            if contained.count("no") > 0:
                return 0
            else:
                for c in contained:
                    count += int(c[0]) * (solve(c[2:]) + 1)
    return count

print(solve("shiny gold"))
