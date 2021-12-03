f = open('day3.input').read()
lines = f.split('\n')[:-1]

gamma_rate_digits = []
eps_rate_digits = []

for i in range(len(lines[0])):
    no_zeros = 0
    no_ones = 0
    for line in lines:
        ith_digit = line[i]
        if ith_digit == '0':
            no_zeros = no_zeros + 1
        else:
            no_ones = no_ones + 1
    if no_zeros > no_ones:
        most_common = 0
        least_common = 1
    elif no_ones > no_zeros:
        most_common = 1
        least_common = 0
    gamma_rate_digits.append(most_common)
    eps_rate_digits.append(least_common)

#print(gamma_rate_digits, eps_rate_digits)


# Question 2 
possible_oxy_rating = lines.copy()
possible_co2_rating = lines.copy()

def get_zeros_ones(lines,index,tie_breaker_value,check):
    no_zeros = 0
    no_ones = 0
    result = []
    for line in lines:
        ith_digit = line[index]
        if ith_digit == '0':
            no_zeros = no_zeros + 1
        else:
            no_ones = no_ones + 1
    if no_zeros > no_ones:
        most_common = '0'
        least_common = '1'
    elif no_ones > no_zeros:
        most_common = '1' 
        least_common = '0'
    else:
        most_common = tie_breaker_value
        least_common = tie_breaker_value

    print(most_common)
    for line in lines:
        ith_digit = line[index]
        if check == 'most common' and ith_digit == most_common:
            result.append(line)
        elif check == 'least common' and ith_digit == least_common:
            result.append(line)
    return result 


print(possible_oxy_rating)
while(len(possible_oxy_rating) > 1):
    for i in range(len(possible_oxy_rating[0])):
        possible_oxy_rating = get_zeros_ones(possible_oxy_rating,i,'1','most common')
        if len(possible_oxy_rating) == 1:
            break

while(len(possible_co2_rating) > 1):
    for i in range(len(possible_co2_rating[0])):
        possible_co2_rating = get_zeros_ones(possible_co2_rating,i,'0','least common')
        if len(possible_co2_rating) == 1:
            break

print(possible_oxy_rating[0],possible_co2_rating[0])
oxy_rating = int(possible_oxy_rating[0],2)
co2_rating = int(possible_co2_rating[0],2)
print(oxy_rating,co2_rating)
print(oxy_rating * co2_rating)
