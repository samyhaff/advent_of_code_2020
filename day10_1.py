with open("input10", "r") as f:
    f_content = f.read()

adapters = f_content.strip().split("\n")
adapters = [int(x) for x in adapters] 
adapters = [0] + adapters + [max(adapters) + 3]

adapters.sort()
diff_1 = 0
diff_3 = 0

for i in range(1, len(adapters)):
    if adapters[i] - adapters[i - 1] == 1:
        diff_1 += 1
    elif adapters[i] - adapters[i - 1] == 3:
        diff_3 += 1

print(diff_1 * diff_3)
