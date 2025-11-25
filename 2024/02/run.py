res = 0

with open("input.txt", mode = 'r', encoding = "utf8") as file:
    for lines in file :
        line = lines.split()
        l = [int(e) for e in line]
        sens = 0
        if l[0]>l[1] :
            sens = 1
        for i in range(1, len(l)) :
            if not (1<=abs(l[i]-l[i-1])<=3) or (sens and l[i]>=l[i-1]) or (not sens and l[i]<=l[i-1]) :
                break
        else :
            res+=1

print(res)