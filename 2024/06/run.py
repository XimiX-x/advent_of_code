res = 0
matrix = []
pos = [0,0]
di = [-1, 0]

with open ('input.txt', encoding = "utf-8") as file :
    i = 0
    for lines in file :
        matrix.append(list(lines))
        if '^' in lines :
            pos[0] = i
            j = 0
            for elem in lines :
                if elem == '^' :
                    pos[1] = j
                    break
                j += 1
        i += 1

while 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[pos[0]])-1 :
    i, j = pos
    match matrix[i][j] :
        case '.' :
            res += 1
            pos[0] += di[0]
            pos[1] += di[1]
            matrix[i][j] = 'X'
        case '^' :
            res += 1
            pos[0] += di[0]
            pos[1] += di[1]
            matrix[i][j] = 'X'
        case '#' :
            if di[0] == 1 :
                pos[0] -=1
                di[0] = 0
                di[1] = -1
                pos[1] -= 1
            elif di[0] == -1 :
                pos[0] +=1
                di[0] = 0
                di[1] = +1
                pos[1] += 1
            else :
                if di[1] == 1 :
                    pos[0] +=1
                    di[0] = 1
                    di[1] = 0
                    pos[1] -= 1
                else :
                    pos[0] -=1
                    di[0] = -1
                    di[1] = 0
                    pos[1] += 1
        case 'X' :
            pos[0] += di[0]
            pos[1] += di[1]

print(res)
