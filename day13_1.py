from math import *

with open("input13", "r") as f:
    f_content = f.read()

time, ids = f_content.strip().split("\n")
time = int(time)
ids = ids.split(",")
ids = [int(n) for n in ids if n != 'x']

timestamps = [n * ceil(time / n) for n in ids]
print(ids[timestamps.index(min(timestamps))] * (min(timestamps) - time))
