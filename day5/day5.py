lines_parse = open('day5.input').read().split('\n')[:-1]
lines = []
horizontal_vertical_lines = []
diagonal_lines = []
max_rows,max_cols = -1,-1

for line in lines_parse:
    start,end = line.split(' -> ') 
    start_x,start_y = start.split(',')
    end_x,end_y = end.split(',')
    
    coord = ((int(start_x),int(start_y)),(int(end_x),int(end_y)))
    lines.append(coord)

for line in lines:
    start,end = line 
    if start[0] == end[0] or start[1] == end[1]:
        horizontal_vertical_lines.append(line)
    else:
        diagonal_lines.append(line)
    if start[0] > max_rows:
        max_rows = start[0]
    if end[0] > max_rows:
        max_rows = end[0]

    if start[1] > max_cols:
        max_cols = start[1]
    if end[1] > max_cols:
        max_cols = end[1]
max_rows = max_rows + 1
max_cols = max_cols + 1
matrix = [[0 for j in range(max_cols)] for i in range(max_rows)]

for line in horizontal_vertical_lines:
    start,end = line 
    start_x,start_y = start
    end_x,end_y = end 

    if start_y == end_y:
        #vertical line 
        if start_x > end_x:
            for i in range(end_x,start_x+1):
                matrix[i][end_y] = matrix[i][end_y] + 1
        else:
            for i in range(start_x,end_x+1):
                matrix[i][end_y] = matrix[i][end_y] + 1 

    else:
        #horizontal line 
        if start_y > end_y:
            for j in range(end_y,start_y+1):
                matrix[start_x][j] = matrix[start_x][j] + 1 
        else:
            for j in range(start_y,end_y+1):
                matrix[start_x][j] = matrix[start_x][j] + 1 

# only considering vertical and horizontal lines 
total_counts_greater_than_2 = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] >= 2:
            total_counts_greater_than_2 = total_counts_greater_than_2 + 1 

# print(total_counts_greater_than_2)

# Consider diagonal lines 
for line in diagonal_lines:
    start,end = line 
    start_x,start_y = start
    end_x,end_y = end 
    x_diff = 0
    y_diff = 0
    if start_x > end_x:
        x_diff = -1 
    else:
        x_diff = 1 
    if start_y > end_y:
        y_diff = -1
    else:
        y_diff = 1

    for i in range(0,max(start_x-end_x,end_x-start_x)+1):
        point_x = start_x + x_diff * i 
        point_y = start_y + y_diff * i 
        matrix[point_x][point_y] = matrix[point_x][point_y] + 1 

total_counts = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] >= 2:
            total_counts= total_counts+ 1
print(total_counts)
 
