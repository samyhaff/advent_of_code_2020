with open('input4', 'r') as f:
    entries = f.readlines()

valid_count = 0
needed_fields = {
    "byr": 0,
    "iyr": 0,
    "eyr": 0,
    "hgt": 0,
    "hcl": 0,
    "ecl": 0,
    "pid": 0
}
fields = []

for entry in entries:
    if entry != "\n":
        liste = entry.split(" ")
        fields += liste
    else:
        for field in fields:
            field_name, _ = field.split(":")
            if field_name != "cid":
                needed_fields[field_name] = 1
        if list(needed_fields.values()) == [1] * 7:
            valid_count += 1
        needed_fields = {
            "byr": 0,
            "iyr": 0,
            "eyr": 0,
            "hgt": 0,
            "hcl": 0,
            "ecl": 0,
            "pid": 0
        }
        fields = []

print(valid_count)
