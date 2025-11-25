def index(elem, liste) :
    for pos, e in enumerate(liste) :
        if elem == e :
            return pos

def up(sup) :
    return sup in "|F7S"

def down(dow) :
    return dow in "|LJS"

def left(le) :
    return le in "-SFL"

def right(ri) :
    return ri in "-7SJ"

def trouve(dep, maze) :
    le = u = False
    cycle = [x for x in dep]
    while  True :
        x, y = cycle[-1]
        match maze[x][y] :
            case "|" :
                if x>0 and cycle[-2][0] == x+1 and up(maze[x-1][y]):
                    if maze[x-1][y] == "S" :
                        return cycle
                    cycle.append((x-1, y))
                elif x<len(maze)-1 and cycle[-2][0] == x-1 and down(maze[x+1][y]):
                    if maze[x+1][y] == "S" :
                        return cycle
                    cycle.append((x+1, y))
                else :
                    cycle = [x for x in dep]
            case "-" :
                if y>0 and cycle[-2][1] == y+1 and left(maze[x][y-1]):
                    if maze[x][y-1] == "S" :
                        return cycle
                    cycle.append((x, y-1))
                elif y<len(maze[x])-1 and cycle[-2][1] == y-1 and right(maze[x][y+1]) :
                    if maze[x][y+1] == "S" :
                        return cycle
                    cycle.append((x, y+1))
                else :
                    cycle = [x for x in dep]
            case "L" :
                if x>0 and cycle[-2][1] == y+1 and up(maze[x-1][y]):
                    if maze[x-1][y] == "S" :
                        return cycle
                    cycle.append((x-1, y))
                elif y<len(maze[x])-1 and cycle[-2][0] == x-1 and right(maze[x][y+1]):
                    if maze[x][y+1] == "S" :
                        return cycle
                    cycle.append((x, y+1))
                else :
                    cycle = [x for x in dep]
            case "J" :
                if x>0 and cycle[-2][1] == y-1 and up(maze[x-1][y]):
                    if maze[x-1][y] == "S" :
                        return cycle
                    cycle.append((x-1, y))
                elif y>0 and cycle[-2][0] == x-1 and left(maze[x][y-1]):
                    if maze[x][y-1] == "S" :
                        return cycle
                    cycle.append((x, y-1))
                else :
                    cycle = [x for x in dep]
            case "7" :
                if y>0 and cycle[-2][0] == x+1 and left(maze[x][y-1]):
                    if maze[x][y-1] == "S" :
                        return cycle
                    cycle.append((x, y-1))
                elif x<len(maze)-1 and cycle[-2][1] == y-1 and down(maze[x+1][y]):
                    if maze[x+1][y] == "S" :
                        return cycle
                    cycle.append((x+1, y))
                else :
                    cycle = [x for x in dep]
            case "F" :
                if x<len(maze)-1 and cycle[-2][1] == y+1 and down(maze[x+1][y]):
                    if maze[x+1][y] == "S" :
                        return cycle
                    cycle.append((x+1, y))
                elif y<len(maze[x])-1 and cycle[-2][0] == x+1 and right(maze[x][y+1]):
                    if maze[x][y+1] == "S" :
                        return cycle
                    cycle.append((x, y+1))
                else :
                    cycle = [x for x in dep]
            case "S" :
                if y>0 and not le:
                    le = True
                    if left(maze[x][y-1]) :
                        cycle.append((x, y-1))
                elif x>0 and not u:
                    u = True
                    if up(maze[x-1][y]) :
                        cycle.append((x-1, y))
                elif y<len(maze[x])-1 :
                    if right(maze[x][y+1]) :
                        cycle.append((x, y+1))

def main() :
    text = []
    with open("input", encoding = "utf-8") as file :
        li = 0
        for line in file :
            if "S" in line :
                start = li, index("S", line)
            li += 1
            text.append(line)
    cycle = [start]
    cycle = trouve(cycle, text)
    print(len(cycle)//2)

main()