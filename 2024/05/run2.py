import re

dic = {}
flag = False
res = 0

with open ("input.txt", encoding = "utf-8") as file :
    for lines in file :
        if not flag and len(lines)>1 :
            num = re.split("\|", lines)
            if int(num[1]) in dic :
                dic[int(num[1])].append(int(num[0]))
            else :
                dic[int(num[1])] = [int(num[0])]
        else :
            flag = True

        if flag and len(lines)>1 :
            change = False
            num = re.split(",", lines)
            num = [int(elem) for elem in num]
            i = 0
            while i<len(num) :
                elem = num[i]
                j = i+1
                if elem in dic :
                    while j<len(num) :
                        if num[j] in dic[elem] :
                            break
                        j += 1
                else :
                    j = len(num)
                if j<len(num) :
                    change = True
                    temp = num[i]
                    num[i] = num[j]
                    num[j] = temp
                else :
                    i += 1
            if change :
                res += num[len(num)//2]

print(res)
