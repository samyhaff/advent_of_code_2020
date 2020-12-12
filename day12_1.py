from numpy import abs

with open("input12", "r") as f:
    f_content = f.read()

instructions = f_content.strip().split("\n")

def solve():
    directions = [0, 0, 0, 0]
    direction = 1
    convert = {"N": 0, "E": 1, "S": 2, "W": 3}
    for instruction in instructions:
        nav, value = instruction[0], int("".join(instruction[1:]))
        if nav in ["N", "E", "S", "W"]:
            directions[convert[nav]] += value 
        else:
            if nav == "F":
                directions[direction] += value
            elif nav == "R":
                direction = (direction + value // 90) % 4
            else:
                direction = (direction - value // 90) % 4
    return directions 

def distance(liste):
    return abs(liste[0] - liste[2]) + abs(liste[1] - liste[3])

print(distance(solve()))
