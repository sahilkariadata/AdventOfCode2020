from day8_1 import inst_array
instructions = open("day8data.txt").read().splitlines()

def instrchange(no):
    instructionset = open("day8data.txt").read().splitlines()
    oper, arg = instructionset[no].split()
    if oper == 'jmp':
        instructionset[no] = str('nop ' + arg)
        return instructionset
    elif oper == 'nop':
        instructionset[no] = str('jmp ' + arg)
        return instructionset
    else:
        print("error")

jmpnoparray = []
for i in inst_array:
    oper, arg = instructions[i].split()
    if oper == 'jmp' or oper == 'nop':
        jmpnoparray.append(i)


for j in jmpnoparray:
    accumulator = 0
    inst_num = 0
    inst_array = []
    new_instructions = instrchange(j)
    #print(new_instructions)
    while inst_num not in inst_array:
        oper, arg = new_instructions[inst_num].split()
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
        if inst_num >= len(new_instructions):
            print(accumulator)
            break
        

