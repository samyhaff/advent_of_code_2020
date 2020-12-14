from math import ceil
with open("input13", "r") as f:
    f_content = f.read()

_, ids = f_content.strip().split("\n")
ids = ids.split(",")

def test(n):
    for i in range(1, len(ids)):
        bus_id = ids[i]
        if bus_id != 'x' and (n + i) % int(bus_id) != 0:
            return False 
    return True

n = int(ids[0])
while not test(n):
    n += int(ids[0]) 
print(n)
