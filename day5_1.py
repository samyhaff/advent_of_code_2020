with open('input5', 'r') as f:
    f_content = f.readlines()
strings = [chaine.strip() for chaine in f_content]

def row(chaine):
    a = 0
    b = 127
    for i in range(7):
        if chaine[i] == "F":
            b = (a + b) // 2
        else:
            a = (a + b) // 2
    return b

def column(chaine):
    a = 0
    b = 7
    for i in range(3):
        if chaine[i] == "L":
            b = (a + b) // 2
        else:
            a = (a + b) // 2
    return b

maxi = 0
for chaine in strings:
    seat_row = row(chaine[:7])
    seat_column = column(chaine[7:])
    seat_id = seat_row * 8 + seat_column
    if seat_id > maxi:
        maxi = seat_id 

print(maxi)
