lines = open('day10.input').read().split('\n')[:-1]

mapping = {
         '(':')',
         '[':']',
         '<':'>',
         '{':'}'
        }
corrupted = [')',']','>','}']

score_mapping = {
         ')':3,
         ']':57,
         '}':1197,
         '>':25137
        }

def check_corrupted(line):
    stack = []
    is_corrupted = False
    elem_corrupted = None
    for character in line:
        if len(stack) != 0:
            top_item = stack.pop()
            if top_item not in mapping:
                is_corrupted = True
                return is_corrupted,top_item 
            if mapping[top_item] == character:
                continue 
            else:
                stack.append(top_item)
                stack.append(character)
        else:
            stack.append(character)
    return is_corrupted,elem_corrupted 
    
corrupted = []
total_score = 0 
for line in lines:
    corrupt,elem = check_corrupted(line)
    if corrupt:
        total_score = total_score + score_mapping[elem]


print(total_score)
