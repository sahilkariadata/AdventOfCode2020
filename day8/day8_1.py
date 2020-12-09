instructions = open("day8data.txt").read().splitlines()
accumulator = 0

inst_num = 0
inst_array = []
while inst_num not in inst_array:
    oper, arg = instructions[inst_num].split()
    if oper == 'acc':
        accumulator += int(arg)
        inst_array.append(inst_num)
        inst_num += 1
    elif oper == 'jmp':
        inst_array.append(inst_num)
        inst_num += int(arg)
    elif oper == "nop":
        inst_array.append(inst_num)
        inst_num += 1

print(accumulator)
print(inst_array)


