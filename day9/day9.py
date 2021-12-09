lines = open('day9.input').read().split('\n')[:-1]
matrix = []
for line in lines:
    row = []
    for point in line:
        row.append(int(point))
    matrix.append(row)


def check_low_point(matrix,x,y):
    m = len(matrix)
    n = len(matrix[0])
    xes = [-1,1,0,0]
    yes = [0,0,1,-1]
    poss = []
    current_value = matrix[x][y]
    
    for i in range(len(xes)):
        new_x = x+xes[i]
        new_y = y+yes[i]
        if new_x >= 0 and new_y >= 0:
            if new_x < m and new_y < n:
                poss.append((new_x,new_y))

    low_point = True
    for po in poss:
        if matrix[po[0]][po[1]] <= current_value:
            low_point = False
            break
    return low_point

m = len(matrix)
n = len(matrix[0])
low_points = []
low_points_values = []
for i in range(m):
    for j in range(n):
        is_low_point = check_low_point(matrix,i,j)
        if is_low_point:
            low_points.append((i,j))
            low_points_values.append(matrix[i][j])

print(low_points)
print(low_points_values)

result = 0
for value in low_points_values:
    result = result + value + 1 

print(result)
