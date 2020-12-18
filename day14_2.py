with open("input14", "r") as f:
    f_content = f.read()

f_content = f_content.strip().split("\n")
mem = {}

def toBinary(n):
    if n == 1 or n == 0:
        return str(n)
    return toBinary(n // 2) + str(n % 2)

def applyMask(position, mask):
    result = ["0"] * 36
    for i in range(len(mask)):
        if mask[i] == "0":
            result[i] = position[i] 
        elif mask[i] == "1":
            result[i] = "1"
        else: 
            result[i] = "X"
    return "".join(result)

def possibilities(position):
    if "X" not in position:
        return [position]
    for i in range(len(position)):
        if position[i] == "X":
            return [position[:i] + "1" + x for x in possibilities(position[i+1:])] + [position[:i] + "0" + x for x in possibilities(position[i+1:])]

for instruction in f_content:
    if "mask" in instruction: 
        _, mask = instruction.split("=")
        mask = mask.strip()
    else:
        instruction = instruction.split("=")
        value = int(instruction[1])
        position = int(instruction[0].strip()[4:-1])
        position = "".join(["0"] * (36 -len(toBinary(position)))) + toBinary(position)
        for pos in possibilities(applyMask(position, mask)):
            mem[int(pos, 2)] = value

print(sum(mem.values()))
