pw_data = open("day2data.txt").read().splitlines()
num = len(pw_data)
valid_p = 0

for i in range(num):
    cond, password = pw_data[i].split(":")
    limits, letter = cond.split()
    lower, upper = limits.split("-")
    counter = password.count(letter)
    if int(lower) <= counter <= int(upper):
        valid_p += 1

print(valid_p)
