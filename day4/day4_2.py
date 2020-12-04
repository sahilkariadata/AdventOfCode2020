from day4_1 import valid_passports

#function to run through extra conditions
#I thought about using a switch-case type statement
def passport_check(check):
    checklist = []
    for i in range(len(check)):
        if check[i][0] == 'byr':
            if 1920 <= int(check[i][1]) <= 2002:
                checklist.append(True)
            else:
                return False

        elif check[i][0] == 'iyr':
            if 2010 <= int(check[i][1]) <= 2020:
                checklist.append(True)
            else:
                return False

        elif check[i][0] == 'eyr':
            if 2020 <= int(check[i][1]) <= 2030:
                checklist.append(True)
            else:
                return False

        elif check[i][0] == 'hgt':
            if check[i][1][-2:] == 'cm':
                if 150 <= int(check[i][1][:-2]) <= 193:
                    checklist.append(True)
                else:
                    return False

            elif check[i][1][-2:] == 'in':
                if 59 <= int(check[i][1][:-2]) <= 76:
                    checklist.append(True)
                else:
                    return False
            else:
                return False

        elif check[i][0] == 'hcl':
            allowed_chars = {'#','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}
            if len(check[i][1]) == 7 and allowed_chars.issuperset(check[i][1]):
                checklist.append(True)
            else:
                return False

        elif check[i][0] == 'ecl':
            eyeopts = {'amb','blu','brn','gry','grn','hzl','oth'}
            if check[i][1] in eyeopts:
                checklist.append(True)
            else:
                return False

        elif check[i][0] == 'pid':
            if len(check[i][1]) == 9:
                checklist.append(True)
            else:
                return False

        elif check[i][0] == 'cid':
            checklist.append(True)
        else:
            print("An error has occurred")
        
    return(all(checklist))

new_validnum = 0
for j in range(len(valid_passports)):
    if passport_check(valid_passports[j]):
        new_validnum += 1

print(new_validnum)
        


