with open("input10", "r") as f:
    f_content = f.read()

adapters = f_content.strip().split("\n")
adapters = [int(x) for x in adapters] 
adapters = [0] + adapters + [max(adapters) + 3]

adapters.sort()

def valid(liste):
    for i in range(0, len(liste) - 1):
        if liste[i + 1] - liste[i] > 3:
            return False 
    return True

cache = {}

def solve(liste):
    if str(liste) in cache:
        return cache[str(liste)]
    alternatives = []
    if len(liste) < (max(adapters) // 3) + 1:
        return []
    for adapter in liste:
        if adapter != adapters[-1] and adapter != 0:
            new_liste = liste[:]
            new_liste.remove(adapter)
            if valid(new_liste):
                alternatives += [new_liste] + solve(new_liste)
    cache[str(liste)] = alternatives
    return alternatives

solution = solve(adapters)
viewed = []
count = 1
for x in solution:
    if x not in viewed:
        count += 1
        viewed.append(x)
print(count)
