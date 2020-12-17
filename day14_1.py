with open("input14", "r") as f:
    f_content = f.read()

input = f_content.strip().split("\n")
mem = {}

def bitmask(mask, value):
    result = 0
    for i, bit in enumerate(reversed(mask)):
        if bit == "X":
            result += value & (1 << i)
        else:
            result += int(bit) << i 
    return result 

for instruction in input:
    if "mask" in instruction: 
        _, mask = instruction.split("=")
        mask = mask.strip()
    else:
        instruction = instruction.split("=")
        value = int(instruction[1])
        position = int(instruction[0].strip()[4:-1])
        mem[position] = bitmask(mask, value)

print(sum(mem.values()))
