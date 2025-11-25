import copy

def isALoop(mat, x, y, dire, start) :
    i2, j2 = x, y
    i_obst = x + dire[0]
    j_obst = y + dire[1]
    if 0 <= i_obst < len(mat) and 0 <= j_obst < len(mat[i_obst])-1 and mat[i_obst][j_obst] != '#' and not (i_obst, j_obst) in start:
        mat[i_obst][j_obst] = '#'
    else :
        return False
    x_cpt = 0
    while 0 <= i2 < len(mat) and 0<= j2 < len(mat[i2])-1 :
        match mat[i2][j2] :
            case '.' :
                mat[i2][j2] = 'X'
                x_cpt = 0
                i2 += dire[0]
                j2 += dire[1]
            case 'X' :
                if x_cpt >= len(matrix)*len(matrix[i_obst]):
                    start.append((i_obst, j_obst))
                    print(i_obst, j_obst)
                    return True
                x_cpt += 1
                i2 += dire[0]
                j2 += dire[1]
            case '#' :
                if dire[0] == 1 :
                    i2 -=1
                    dire[0] = 0
                    dire[1] = -1
                    j2 -= 1
                elif dire[0] == -1 :
                    i2 +=1
                    dire[0] = 0
                    dire[1] = +1
                    j2 += 1
                elif dire[1] == 1 :
                    i2 +=1
                    dire[0] = 1
                    dire[1] = 0
                    j2 -= 1
                else :
                    i2 -=1
                    dire[0] = -1
                    dire[1] = 0
                    j2 += 1
    return False

RES = 0
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

start_pos = [(pos[0], pos[1])]

while 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[pos[0]])-1 :
    i, j = pos
    match matrix[i][j] :
        case '.' :
            pos[0] += di[0]
            pos[1] += di[1]
            if isALoop(copy.deepcopy(matrix), i, j, copy.deepcopy(di), start_pos) :
                RES += 1
        case '^' :
            matrix[i][j] = '.'
        case '#' :
            if di[0] == 1 :
                pos[0] -=1
                di[0] = 0
                di[1] = -1
            elif di[0] == -1 :
                pos[0] +=1
                di[0] = 0
                di[1] = +1
            elif di[1] == 1 :
                di[0] = 1
                di[1] = 0
                pos[1] -= 1
            else :
                di[0] = -1
                di[1] = 0
                pos[1] += 1

print(RES)
