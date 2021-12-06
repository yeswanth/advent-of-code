from collections import defaultdict


f = open('day6-sample.input').read().strip()
fish_timers = [int(x) for x in f.split(',')]
timers_dict = defaultdict(int)

NO_OF_CYCLES = 1 

def next_cycle(timers):
    new_timers = []
    children_fish_timers = []
    for timer in timers:
        if timer > 0:
            new_timers.append(timer-1)
        if timer == 0:
            new_timers.append(6) 
            children_fish_timers.append(8)
    new_timers.extend(children_fish_timers)
    return new_timers


for cycle in range(1,NO_OF_CYCLES+1):
    fish_timers = next_cycle(fish_timers)

print(len(fish_timers))
