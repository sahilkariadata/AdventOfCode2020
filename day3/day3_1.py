import math
def treecalc(right, down):
    mapinput = open("day3data.txt").read().splitlines()
    num = len(mapinput)

    actspace = math.ceil(num/down) #number of actions required to reach bottom
    copynum = math.ceil((right*actspace)/len(mapinput[0])) #number of copies to be concatenated

    for i in range(num):
        mapinput[i] = mapinput[i] * copynum

    treenum = 0

    for j in range(actspace):
        if (mapinput[down*j][right*j]) == '#':
            treenum += 1

    return(treenum)

print(treecalc(3,1))

