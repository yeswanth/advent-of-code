f = open('day2.input').read()
lines = f.split('\n')[:-1]

horizontal = 0
depth = 0
aim = 0
for line in lines:
    direction, number = line.split(' ')
    number = int(number)
    if direction == 'forward':
        horizontal = horizontal + number 
        depth = depth + number*aim
    elif direction == 'down':
        #depth = depth + number 
        aim = aim + number 
    elif direction == 'up':
        #depth = depth - number
        aim = aim - number 
    print(line,horizontal,depth,aim)
print(horizontal*depth)
