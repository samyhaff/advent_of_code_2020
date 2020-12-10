with open("input10", "r") as f:
    f_content = f.read()

adapters = f_content.strip().split("\n")
adapters = [int(x) for x in adapters] 
adapters = [0] + adapters + [max(adapters) + 3]

adapters.sort()

cache = {}
def solve(i):
    if i in cache:
        return cache[i]
    if i == len(adapters) - 1:
        return 1
    counter = 0
    for j in range(i + 1, len(adapters)):
        if adapters[j] - adapters[i] <= 3:
            counter += solve(j)
    cache[i] = counter
    return counter

print(solve(0))
