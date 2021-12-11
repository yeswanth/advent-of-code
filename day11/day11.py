lines = open('day11.input').read().split('\n')[:-1]
matrix = []
for line in lines:
    row = []
    for elem in line:
        row.append(int(elem))
    matrix.append(row)

def get_neighbours(matrix,x,y):
    m = len(matrix)
    n = len(matrix[0])
    xes = [1,-1,0,0,-1,1,-1,1]
    yes = [0,0,1,-1,-1,-1,1,1]
    valid_neighbours = []
    for i in range(len(xes)):
        new_x = x + xes[i]
        new_y = y + yes[i]
        if new_x >= 0 and new_y >= 0 and new_x < m and new_y < n:
            valid_neighbours.append((new_x,new_y))
    return valid_neighbours


from collections import deque
def increase_number(matrix,i,j,flashed):
    queue = deque()
    queue.append((i,j))
    while len(queue) > 0:
        x,y = queue.popleft()
        if matrix[x][y] != 9:
            if (x,y) not in flashed:
                matrix[x][y] = matrix[x][y] + 1
        else:
            matrix[x][y] = 0
            flashed.append((x,y))
            neighbours = get_neighbours(matrix,x,y)
            for neighbour in neighbours:
                if neighbour not in flashed:
                    queue.append(neighbour)
    


def run_step(matrix):
    m = len(matrix)
    n = len(matrix[0])
    flashed = []
    for i in range(m):
        new_row = []
        for j in range(n):
            value = matrix[i][j]
            increase_number(matrix,i,j,flashed)
    return matrix,len(flashed) 

def is_matrix_0(matrix):
    m = len(matrix)
    n = len(matrix[0])
    matrix_zero = True
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != 0:
                matrix_zero = False
                return matrix_zero
    return matrix_zero


""" Part A
NO_OF_STEPS = 100 
total_flashes = 0
for i in range(NO_OF_STEPS):
    matrix,flashes = run_step(matrix)
    total_flashes = total_flashes + flashes

#print(total_flashes)
"""

NO_OF_STEPS = 1000
for i in range(NO_OF_STEPS):
    matrix,flashes = run_step(matrix)
    if is_matrix_0(matrix):
        break
print(i+1)



            
