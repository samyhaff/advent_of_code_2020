with open("input9", "r") as f:
    f_content = f.read()

numbers = f_content.strip().split("\n")
numbers = [int(x) for x in numbers]

def test(preamble, number):
    for i in range(25):
        for j in range(i + 1, 25):
            if preamble[i] + preamble[j] == number:
                return True
    return False

def solve():
    for i in range(25, len(numbers)):
        preamble = numbers[i - 25 : i]
        if not test(preamble, numbers[i]):
            return numbers[i]

print(solve())
