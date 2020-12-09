with open("input8", "r") as f:
    f_content = f.read()

instructions = f_content.split("\n")[:-1]

def test(instruction_set):
    acc = 0
    pointer = 0
    visited = []
    while pointer not in visited and pointer < len(instruction_set):
        visited.append(pointer)
        instruction = instruction_set[pointer]
        instr, value = instruction.split(" ")
        value = int(value)
        if instr == "acc":
            acc += value
            pointer += 1
        elif instr == "jmp":
            pointer += value
        else:
            pointer += 1
    if pointer >= len(instruction_set):
        return True, acc 
    return False, -1

def solve():
    for i in range(len(instructions)):
        new_instructions = instructions[:]
        instr, param = instructions[i].split(" ")
        if instr == "jmp":
           new_instructions[i] = " ".join(["nop", param])
           condition, acc = test(new_instructions)
           if condition:
               return acc
        elif instr == "nop" and "param" != "+0" and "param" != "-0":
            new_instructions[i] = " ".join(["jmp", param])
            condition, acc = test(new_instructions)
            if condition:
                return acc

print(solve())
