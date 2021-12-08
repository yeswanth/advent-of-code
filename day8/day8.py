lines = open('day8.input').read().split('\n')[:-1]
parsed_input = []
for line in lines:
    unique_signals = line.split('|')[0]
    number = line.split('|')[1].strip()
    parsed_input.append((unique_signals,number),)

count_easy_digits = 0
easy_digits_signal_numbers = [2,3,4,7]
for inp in parsed_input:
    output_value = inp[1]
    digits = output_value.split(' ')
    for digit in digits:
        if len(digit) in easy_digits_signal_numbers:
            count_easy_digits = count_easy_digits + 1
print(count_easy_digits)

