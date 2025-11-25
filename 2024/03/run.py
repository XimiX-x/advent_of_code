import re

res = 0

with open ("input.txt", mode  = 'r', encoding = "utf-8") as file :
    for lines in file :
        liste = re.findall("((mul)\(([0-9]|[0-9][0-9]|[0-9][0-9][0-9]),([0-9]|[0-9][0-9]|[0-9][0-9][0-9])\))",lines)
        for e in liste :
            res += int(e[2])*int(e[3])

print(res)