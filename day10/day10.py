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
    
non_corrupt = []
total_score = 0 
for line in lines:
    corrupt,elem = check_corrupted(line)
    if corrupt:
        total_score = total_score + score_mapping[elem]
    else:
        non_corrupt.append(line)

#print(total_score)

incomplete_mapping = {
        ')':1,
        ']':2,
        '}':3,
        '>':4
        }

def determine_incomplete(line):
    stack = []
    is_corrupted = False
    for character in line:
        if len(stack) != 0:
            top_item = stack.pop()
            if mapping[top_item] == character:
                continue 
            else:
                stack.append(top_item)
                stack.append(character)
        else:
            stack.append(character)

    print(stack)
    items_added = []
    while(len(stack)) > 0:
        item = stack.pop()
        items_added.append(mapping[item])
    print(items_added)
    return items_added

def calculate_score(items_added):
    total_score = 0
    for i in items_added:
        score = incomplete_mapping[i]
        total_score = total_score * 5 + score
    return total_score 

scores = []
for line in non_corrupt:
    items_added = determine_incomplete(line)
    score = calculate_score(items_added)
    scores.append(score)

scores.sort()
middle = len(scores)//2
print(scores[middle])
