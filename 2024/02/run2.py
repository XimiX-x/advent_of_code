res = 0

def isValide(l, f) :
    sens = l[0]>l[1]
    i = 1
    flag = f
    while i<len(l):
        if not (1<=abs(l[i]-l[i-1])<=3) or (sens and l[i]>=l[i-1]) or (not sens and l[i]<=l[i-1]):
            if flag :
                return False
            else :
                flag = True
                i = i+1
                if i<len(l) :
                    if (isValide(l[0:i-2]+l[i-1:], True)) :
                        return True
                    if isValide(l[0:i-1]+l[i:], True) :
                        return True
                    if i == 3 :
                        if (isValide([l[0]]+l[2:], True)) :
                            return True
                        if (isValide(l[1:], True)) :
                            return True
                    if i == 2 :
                        sens = l[0]>l[2]
                    if not (1<=abs(l[i]-l[i-2])<=3) or (sens and l[i]>=l[i-2]) or (not sens and l[i]<=l[i-2]):
                        if i == 2:
                            return isValide(l[1:], True)
                        else :
                            return False
        i += 1
    return True

with open("input.txt", mode = 'r', encoding = "utf8") as file:
    for lines in file :
        line = lines.split()
        li = [int(e) for e in line]
        
        if isValide(li, False) :
            res += 1

print(res)