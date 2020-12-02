pw_data = open("day2data.txt").read().splitlines()
num = len(pw_data)
valid_p = 0

def xor(cond1,cond2):
    return bool(cond1) ^ bool(cond2)

for i in range(num):
    cond, password = pw_data[i].split(":")
    positions, letter = cond.split()
    pos1, pos2 = positions.split("-")
    if xor(letter == password[int(pos1)],letter == password[int(pos2)]):
        valid_p += 1

print(valid_p)