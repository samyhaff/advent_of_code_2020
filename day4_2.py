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

def condition(needed_fields):
    test_byr = 1920 <= int(needed_fields['byr']) <= 2002
    test_iyr = 2010 <= int(needed_fields['iyr']) <= 2020
    test_eyr = 2020 <= int(needed_fields['eyr']) <= 2030


for entry in entries:
    if entry != "\n":
        liste = entry.split(" ")
        fields += liste
    else:
        for field in fields:
            field_name, field_data = field.split(":")
            field_data = field_data.strip()
            if field_name != "cid":
                needed_fields[field_name] = field_data 
        if condition(needed_fields):
            count += 1
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
