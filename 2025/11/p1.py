#!/usr/bin/env python3.10

g = {}
with open("input") as file :
    for lines in file :
        line = lines.split()
        g[line[0][:-1]] = line[1:]

cour = 'you'
q = []
q.append(cour)
res = 0
while q :
    cour = q.pop()
    if cour == "out" :
        res += 1
    if cour != "out" :
        for suiv in g[cour] :
            q.append(suiv)

print(res)

### No animation today, I'm lazy
