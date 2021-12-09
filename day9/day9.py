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

def get_possibilites(matrix,x,y):
    m = len(matrix)
    n = len(matrix[0])
    xes = [-1,1,0,0]
    yes = [0,0,1,-1]
    poss = []
    for i in range(len(xes)):
        new_x = x+xes[i]
        new_y = y+yes[i]
        if new_x >= 0 and new_y >= 0:
            if new_x < m and new_y < n:
                poss.append((new_x,new_y))

    return poss


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


result = 0
for value in low_points_values:
    result = result + value + 1 

#print(result)
from collections import deque 
def get_basin(matrix,start_x,start_y):
    queue = deque()
    queue.append((start_x,start_y))
    visited = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]

    while(len(queue))>0:
        x,y = queue.popleft()
        visited[x][y] = True
        possibles = get_possibilites(matrix,x,y)
        for possible in possibles:
            new_x = possible[0]
            new_y = possible[1]
            if matrix[new_x][new_y] != 9:
                if visited[new_x][new_y] != True:
                    queue.append((new_x,new_y))

    basin = []
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if visited[i][j]:
                basin.append((i,j),)
    return basin


def are_basins_equal(basin_a,basin_b):
    if len(basin_a) != len(basin_b):
        return False 
    basins_equal = True
    for i in basin_a:
        if i not in basin_b:
            return False
    return True


def check_exists_in_basin(basins,new_basin):
    for basin in basins:
        equal = are_basins_equal(basin,new_basin)
        if equal:
            return True 
    return False 


basins = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] != 9:
            basin = get_basin(matrix,i,j)
            if not check_exists_in_basin(basins,basin):
                basins.append(basin)

score = []
for basin in basins:
    score.append(len(basin))


def sort_index(lst,rev=True):
    index = range(len(lst))
    s = sorted(index, reverse=rev, key=lambda i: lst[i])
    return s

indexs_top_3 = sort_index(score)[:3]
print(indexs_top_3)

mul_score = 1
for i in indexs_top_3: 
    basin = basins[i]
    mul_score = mul_score * len(basin)

print(mul_score)


