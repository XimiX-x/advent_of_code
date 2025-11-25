res = 0
matrix = []

with open("input.txt", encoding = "utf-8") as file :
    for lines in file :
        matrix.append(lines)

for i, elem in enumerate(matrix) :
    j = 0
    while j<len(elem) :
        if elem[j] == "X" :
            if j<len(elem)-3 :
                if i>2 :
                    if matrix[i-1][j+1] == "M" and matrix[i-2][j+2] == "A" and matrix[i-3][j+3] == "S" :
                        res += 1
                if elem[j+1] == "M" and elem[j+2] == "A" and elem[j+3] == "S" :
                    res += 1
                if i<len(matrix)-3 :
                    if matrix[i+1][j+1] == "M" and matrix[i+2][j+2] == "A" and matrix[i+3][j+3] == "S" :
                        res += 1
            if i<len(matrix)-3 :
                if matrix[i+1][j] == "M" and matrix[i+2][j] == "A" and matrix[i+3][j] == "S" :
                    res += 1
            if j>2 :
                if i<len(matrix)-3 :
                    if matrix[i+1][j-1] == "M" and matrix[i+2][j-2] == "A" and matrix[i+3][j-3] == "S" :
                        res += 1
                if elem[j-1] == "M" and elem[j-2] == "A" and elem[j-3] == "S" :
                    res += 1
                if i>2 :
                    if matrix[i-1][j-1] == "M" and matrix[i-2][j-2] == "A" and matrix[i-3][j-3] == "S" :
                        res = res+1
            if i>2 :
                if matrix[i-1][j] == "M" and matrix[i-2][j] == "A" and matrix[i-3][j] == "S" :
                    res = res+1
        j += 1

print(res)