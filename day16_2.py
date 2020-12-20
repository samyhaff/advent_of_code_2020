with open("input16", "r") as f:
    f_content = f.read()

rules, my_ticket, nearby_tickets = f_content.strip().split("\n\n")
my_ticket = my_ticket.split("\n")[1]
nearby_tickets = nearby_tickets.split("\n")[1:]
my_ticket = [int(x) for x in my_ticket.split(",")]
nearby_tickets = [[int(x) for x in y.split(",")] for y in nearby_tickets]
rules = rules.split("\n")
rules = [rule[rule.index(":")+1:].strip().split(" ") for rule in rules]

ranges = []
for rule in rules:
    range1, range2 = rule[0], rule[2]
    range1 = range1.split("-")
    range2 = range2.split("-")
    ranges += [int(x) for x in range1] + [int(x) for x in range2]

def check_field(field):
    for i in range(len(ranges) - 1):
        if ranges[i] <= field <= ranges[i + 1]:
            return True 
    return False

def check_ticket(ticket):
    for field in ticket:
        if not check_field(field):
            return False 
    return True

def remove_invalid(nearby_tickets):
    valid = []
    for ticket in nearby_tickets:
        if check_ticket(ticket):
            valid.append(ticket)
    return valid

nearby_tickets = remove_invalid(nearby_tickets)

"""
Backtracking
"""

solution = [-1] * len(rules) 

def giveEmptyLoc(solution):
    for i in range(len(solution)):
        if solution[i] == -1:
            return i 
    return -1 

def valid(i, v, solution):
    if v in solution:
        return False
    for ticket in range(len(nearby_tickets)):
        if not (ranges[4 * i] <= nearby_tickets[ticket][v] <= ranges[(4 * i) + 1] or ranges[(4 * i) + 2] <= nearby_tickets[ticket][v] <= ranges[(4 * i) + 3]):
            return False 
    return True

def solve(solution):
    if giveEmptyLoc(solution) == -1:
        return solution
    for v in range(len(my_ticket)):
        i = giveEmptyLoc(solution)
        if valid(i, v, solution):
            solution[i] = v 
            if solve(solution):
                return solution
            solution[i] = -1 
    return False

solution = solve(solution)

result = 1 
for i in solution[:6]:
    result *= my_ticket[i]
print(result)
