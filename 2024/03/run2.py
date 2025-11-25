import re

res = 0
enable = 1

with open ("input.txt", mode  = 'r', encoding = "utf-8") as file :
    for lines in file :
        if enable :
            dont = re.split("don't\(\)", lines)
            liste = re.findall("((mul)\(([0-9]|[0-9][0-9]|[0-9][0-9][0-9]),([0-9]|[0-9][0-9]|[0-9][0-9][0-9])\))",dont[0])
            for e in liste :
                res += int(e[2])*int(e[3])
            if len(dont)>1 :
                enable = 0
                for e in dont[1:] :
                    do = re.split("do\(\)", e)
                    if len(do)>1 :
                        enable = 1
                        for txt in do[1:] :
                            liste = re.findall("((mul)\(([0-9]|[0-9][0-9]|[0-9][0-9][0-9]),([0-9]|[0-9][0-9]|[0-9][0-9][0-9])\))",txt)
                            for parse in liste :
                                res += int(parse[2])*int(parse[3])
                    else :
                        enable = 0
        else :
            dont = re.split("don't\(\)", lines)
            for e in dont :
                do = re.split("do\(\)", e)
                if len(do)>1 :
                    enable = 1
                    for txt in do[1:] :
                        liste = re.findall("((mul)\(([0-9]|[0-9][0-9]|[0-9][0-9][0-9]),([0-9]|[0-9][0-9]|[0-9][0-9][0-9])\))",txt)
                        for parse in liste :
                            res += int(parse[2])*int(parse[3])
                else :
                    enable = 0

print(res)