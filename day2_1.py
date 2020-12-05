with open('input2', 'r') as f:
    entries = f.readlines()

count = 0 
for entry in entries:
    interval, lettre, password = entry.split(" ")
    minimum, maximum = interval.split("-")
    minimum, maximum = int(minimum), int(maximum)
    lettre = lettre[0]
    if minimum <= password.count(lettre) <= maximum:
        count += 1

print(count)
