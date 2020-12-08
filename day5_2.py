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

seats_list = []
maxi = 0
mini = 1024
for chaine in strings:
    seat_row = row(chaine[:7])
    seat_column = column(chaine[7:])
    seat_id = seat_row * 8 + seat_column
    seats_list.append(seat_id)
    if seat_id > maxi:
        maxi = seat_id 
    if seat_id < mini:
        mini = seat_id
for seat in range(mini, maxi + 1):
    if (seat not in seats_list) and (seat + 1 in seats_list) and (seat - 1 in seats_list):
        print(seat)
