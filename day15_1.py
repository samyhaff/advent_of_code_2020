numbers = {11: [1], 0: [2], 1: [3], 10: [4], 5: [5], 19: [6]}

last_spoken = 19
turn = 7
while turn <= 30000000:
    if len(numbers[last_spoken]) <= 1:
        last_spoken = 0 
        numbers[0].append(turn)
    else: 
        last_spoken = numbers[last_spoken][-1] - numbers[last_spoken][-2]
        if last_spoken not in numbers.keys():
            numbers[last_spoken] = [turn]
        else:
            numbers[last_spoken].append(turn)
    turn += 1
    
print(last_spoken)
