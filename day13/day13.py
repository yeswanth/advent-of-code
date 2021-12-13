f = open('day13-sample.input').read()
str_lines,str_folds = f.split('\n\n')

dots = []
folds = []
max_x, max_y = -1,-1

for line in str_lines.split('\n'):
    y,x = line.split(',')[0],line.split(',')[1] 
    dots.append((int(x), int(y)))
    if int(x) > max_x:
        max_x = int(x)
    if int(y) > max_y:
        max_y = int(y)

for fold in str_folds.split('\n'):
    splits = fold.strip().split("fold along ")
    if len(splits) > 1:
        dire,value = splits[1].split('=')
        folds.append((dire,int(value)))




matrix = [[0 for j in range(max_y+1)] for i in range(max_x+1)]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if (i,j) in dots:
            matrix[i][j] = 1


def fold_horizontal(matrix,x):
    new_matrix = [[0 for j in range(len(matrix[0]))] for i in range(x)]

    cols = len(matrix[0])
    rows = len(matrix)

    for i in range(x):
        for j in range(len(matrix[0])):
            new_matrix[i][j] = matrix[i][j]

    for i in range(x):
        for j in range(len(matrix[0])):
            if matrix[rows-i-1][j] == 1:
                new_matrix[i][j] = matrix[rows-i-1][j]

    return new_matrix

def fold_vertical(matrix,y):
    new_matrix = [[0 for j in range(y)] for i in range(len(matrix))]

    cols = len(matrix[0])
    rows = len(matrix)

    for i in range(len(matrix)):
        for j in range(y):
            new_matrix[i][j] = matrix[i][j]

    for i in range(len(matrix)):
        for j in range(y):
            if matrix[i][cols-j-1] == 1:
                new_matrix[i][j] = matrix[i][cols-j-1]

    return new_matrix


def count_dots(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                count = count + 1
    return count

def execute_instruction(matrix,dire,value):
    if dire == 'x':
        return fold_vertical(matrix,value) 
    if dire == 'y':
        return fold_horizontal(matrix,value) 

matrix_first_fold = execute_instruction(matrix,folds[0][0],folds[0][1])
#print(count_dots(matrix_first_fold))


