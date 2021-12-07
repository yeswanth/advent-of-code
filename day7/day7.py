import sys
f = open('day7.input').read().strip()
positions = [int(i) for i in f.split(',')]

def fuel_to_final_position(positions,final_position):
    fuel = 0
    for position in positions:
        fuel = fuel + max(position-final_position, final_position-position)
    return fuel 

def fuel_to_final_position_part_b(positions,final_position):
    fuel = 0
    for position in positions:
        diff = abs(position - final_position)
        fuel = fuel + ((diff*(diff+1))/2)
    return fuel 



max_position_possible = max(positions)

min_fuel = sys.maxsize 
for position in range(max_position_possible):
    fuel = fuel_to_final_position(positions,position)
    if fuel < min_fuel: 
        min_fuel = fuel 

# print(min_fuel)

# Part B 
min_fuel = sys.maxsize 
for position in range(max_position_possible):
    fuel = fuel_to_final_position_part_b(positions,position)
    if fuel < min_fuel:
        min_fuel = fuel 

print(int(min_fuel))
