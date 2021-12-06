from collections import defaultdict


f = open('day6.input').read().strip()
fish_timers = [int(x) for x in f.split(',')]
timers_dict = defaultdict(int)
for timer in fish_timers:
    timers_dict[timer] = timers_dict[timer] + 1 


NO_OF_CYCLES = 256 

def next_cycle(timers):
    new_timers_dict = defaultdict(int) 
    for timer,count in timers.items():
        if timer > 0:
            new_timer = timer-1 
            new_timers_dict[new_timer] = new_timers_dict[new_timer] + count 
        if timer == 0:
            new_timer = 6 
            new_timers_dict[new_timer] = new_timers_dict[new_timer] + count 
            new_timers_dict[8] = new_timers_dict[8] + count 
        """
        if timer > 0:
            new_timers.append(timer-1)
        if timer == 0:
            new_timers.append(6) 
            children_fish_timers.append(8)
        """
    return new_timers_dict


for cycle in range(1,NO_OF_CYCLES+1):
    timers_dict = next_cycle(timers_dict)


total_fish = 0
for timer,count in timers_dict.items():
    total_fish = total_fish + count
print(total_fish)


