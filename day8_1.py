with open("input8", "r") as f:
    f_content = f.read()

instructions = f_content.split("\n")[:-1]
acc = 0
pointer = 0
visited = []

while pointer not in visited:
    visited.append(pointer)
    instruction = instructions[pointer].split(" ")
    instr, param = instruction[0], int(instruction[1])
    if instr == "acc":
        acc += param
        pointer += 1
    elif instr == "jmp":
        pointer += param
    else: 
        pointer += 1

print(acc)
