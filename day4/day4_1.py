mapinput = open("day4data.txt").read().split('\n\n')
num = len(mapinput)
req_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
valid_num = 0
valid_passports = []

for i in range(num):
    variables = mapinput[i].split()
    coup_vars = [j.split(':') for j in variables]
    flat_vars = [item for sublist in coup_vars for item in sublist]
    validity = all(field in flat_vars for field in req_fields)
    if validity == True:
        valid_num += 1
        valid_passports.append(coup_vars)

print(valid_num)