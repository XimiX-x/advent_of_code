res = 0
matrix = []

with open("input.txt", encoding = "utf-8") as file :
    for lines in file :
        matrix.append(lines)

i = 1
while i<len(matrix)-1 :
    elem = matrix[i]
    j = 1
    while j<len(elem)-1 :
        if elem[j] == "A" :
            if matrix[i-1][j-1] == matrix[i-1][j+1] == "M" and matrix[i+1][j-1] == matrix[i+1][j+1] == "S" :
                res += 1
            elif matrix[i-1][j-1] == matrix[i+1][j-1] == "M" and matrix[i-1][j+1] == matrix[i+1][j+1] == "S" :
                res += 1
            elif matrix[i-1][j+1] == matrix[i+1][j+1] == "M" and matrix[i-1][j-1] == matrix[i+1][j-1] == "S" :
                res += 1
            elif matrix[i+1][j-1] == matrix[i+1][j+1] == "M" and matrix[i-1][j-1] == matrix[i-1][j+1] == "S" :
                res += 1
        j += 1
    i += 1

print(res)