with open("input10", "r") as f:
    f_content = f.read()

adapters = f_content.strip().split("\n")
adapters = [int(x) for x in adapters] 
adapters = [0] + adapters + [max(adapters) + 3]

adapters.sort()

def valid(liste):
    if len(liste) < 3:
        return False
    for i in range(0, len(liste) - 1):
        if liste[i + 1] - liste[i] > 3:
            return False 
    return True

def solve():
    global adapters
    to_visit = [adapters]
    solution = []
    while to_visit != []:
        test = to_visit[0]
        for adapter in test:
            if adapter != 0 and adapter != adapters[-1]:
                liste = test[:]
                liste.remove(adapter)
                if valid(liste):
                    solution.append(liste)
                    to_visit.append(liste)
        to_visit = to_visit[1:]
    viewed = []
    counting = 1
    for x in solution:
        if x not in viewed:
            counting += 1
            viewed.append(x)
    return counting

print(solve())
