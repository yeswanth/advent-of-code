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

print(gamma_rate_digits, eps_rate_digits)



