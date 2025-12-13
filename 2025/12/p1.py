#!/usr/bin/env python3.10

pieces = {}
res = 0
with open("input") as file :
    for _ in range(6) :
        line = next(file)
        area = 0
        for _ in range(3): 
            piece = next(file)
            for c in piece :
                area += c == "#"
        pieces[int(line[:-2])] = area
        line = next(file)
    
    for lines in file :
        line = lines.split()
        
        empty_space = line[0].split('x')
        empty_space = int(empty_space[0]) * int(empty_space[1][:-1])

        area_piece = 0
        for i in range(6) :
            area_piece += pieces[i]*int(line[i+1])
        
        if area_piece < empty_space :
            res += 1

print(res)

### No animation for this, way too hard
