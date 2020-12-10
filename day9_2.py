with open("input9", "r") as f:
    f_content = f.read()

numbers = f_content.strip().split("\n")
numbers = [int(x) for x in numbers]

missing = 41682220

def solve():
    for pas in range(2, len(numbers)):
        for i in range(len(numbers) - pas):
            if sum(numbers[i: i + pas + 1]) == missing:
                return numbers[i: i + pas + 1]

liste = solve()
print(min(liste) + max(liste))
