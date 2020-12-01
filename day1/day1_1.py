e_report = open("day1data.txt").read().splitlines()
#e_report = [1721,979,366,299,675,1456]
num = len(e_report)
found = 0

for i in range(num):
    for j in range(i+1,num):
        if int(e_report[i]) + int(e_report[j]) == 2020:
            out = int(e_report[i])*int(e_report[j])
            found = 1
            break
    else:
        if found == 1:
            break


print(out)