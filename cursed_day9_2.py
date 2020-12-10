with open("input9", "r") as f:
    f_content = f.read()

numbers = f_content.strip().split("\n")
numbers = [int(x) for x in numbers]
missing = 41682220
numbers.sort()

i = 0
while numbers[i] != missing:
    i += 1
numbers = numbers[:i]

def solve(n):
    if n < numbers[0] + numbers[1]:
        return False, []
    for x in numbers:
        if (n - x in numbers) and (n - x != x):
            return True, [x, n - x]
        cond, l = solve(n - x)
        if cond and (x not in l):
            return True, [x] + l
    return False, []

print(solve(missing))
