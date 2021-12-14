f = open('day14.input').read().split('\n\n')
polymer = f[0]
rules = {} 
lines = f[1].split('\n')[:-1]
for line in lines:
    firstsecond, middle = line.split(' -> ')
    first = firstsecond[0]
    second = firstsecond[1]
    rule = {'first':first,'second':second, 'middle':middle}
    rules[firstsecond] = rule


def process(polymer):
    new_polymer = ''
    for i in range(len(polymer)-1):
        pairelem_1 = polymer[i]
        pairelem_2 = polymer[i+1] 
        pair = pairelem_1 + pairelem_2 
        rule = rules[pair]
        new_polymer = new_polymer + rule['first'] + rule['middle'] 

    new_polymer = new_polymer + rule['second']
    return new_polymer 


from collections import Counter
def count_elements(polymer):
    elem_freq = Counter(polymer)
    most_common_freq = elem_freq.most_common(1)[0][1]
    least_common_freq = elem_freq.most_common()[-1][1]
    return most_common_freq - least_common_freq

    

NO_OF_STEPS = 10 
new_polymer = polymer
for i in range(NO_OF_STEPS):
    print("Step ", i+1)
    new_polymer = process(new_polymer)

print(count_elements(new_polymer))


