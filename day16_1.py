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

def check(field):
    for i in range(len(ranges) - 1):
        if ranges[i] <= field <= ranges[i + 1]:
            return True 
    return False

def solve():
    invalid = []
    for ticket in nearby_tickets:
        for field in ticket:
            if not check(field):
                invalid.append(field)
    return invalid

print(sum([x for x in solve()]))
