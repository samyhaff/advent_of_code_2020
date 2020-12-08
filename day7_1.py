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

def solve():
    deja_vu = []
    a_visiter = ["shiny gold"]
    while a_visiter != []:
        bag = a_visiter[0]
        for container, contained in bags:
            if bag in contained:
                a_visiter.append(container)
        a_visiter = a_visiter[1:]
        deja_vu.append(bag)
    return set(deja_vu)

print(len(solve()) - 1)
