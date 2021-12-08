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
#print(count_easy_digits)

def sort_str(string):
    return ''.join(sorted(string))

def get_mapping(unique_signals_str):
    seg_mapping = {}
    signal_mapping = {}
    signal_number_mapping = {}
    signals = unique_signals_str.split(' ')
    for signal in signals:
        if len(signal) == 2:
            signal_mapping[1] = signal 
            signal_number_mapping[sort_str(signal)] = 1
        if len(signal) == 3:
            signal_mapping[7] = signal 
            signal_number_mapping[sort_str(signal)] = 7
        if len(signal) == 4:
            signal_mapping[4] = signal 
            signal_number_mapping[sort_str(signal)] = 4
        if len(signal) == 7:
            signal_mapping[8] = signal 
            signal_number_mapping[sort_str(signal)] = 8

    # u1 segment 
    for i in signal_mapping[7]:
        if i not in signal_mapping[4]:
            seg_mapping['u1'] = i
            break

    # Mapping for 6 
    signal_lengths_6 = [signal for signal in signals if len(signal) == 6]
    for signal in signal_lengths_6:
        for i in signal_mapping[1]:
            if i not in signal:
                signal_mapping[6] = signal 
                signal_number_mapping[sort_str(signal)] = 6
                break

    # Mapping for r1, r2 
    for i in signal_mapping[1]:
        if i not in signal_mapping[6]:
            seg_mapping['r1'] = i 
        else:
            seg_mapping['r2'] = i

    # Mapping for 2 5 3 
    signal_lengths_5 = [signal for signal in signals if len(signal) == 5]
    for signal in signal_lengths_5:
        if seg_mapping['r1'] in signal:
            if seg_mapping['r2'] in signal:
                signal_mapping[3] = signal 
                signal_number_mapping[sort_str(signal)] = 3
            else:
                signal_mapping[2] = signal 
                signal_number_mapping[sort_str(signal)] = 2
        else:
            signal_mapping[5] = signal
            signal_number_mapping[sort_str(signal)] = 5

    # Mapping for l2
    for i in signal_mapping[8]:
        if i != seg_mapping['r1'] and i not in signal_mapping[5]:
            seg_mapping['r2'] = i
            break

    # Mapping for 0 9 
    signal_lengths_6 = [signal for signal in signals if len(signal) == 6]
    for signal in signal_lengths_6:
        if signal != signal_mapping[6]:
            if seg_mapping['r2'] not in signal:
                signal_mapping[9] = signal 
                signal_number_mapping[sort_str(signal)] = 9
            else:
                signal_mapping[0] = signal
                signal_number_mapping[sort_str(signal)] = 0


    return signal_number_mapping

def decode_string_to_digits(signal_mapping,digits_string):
    result = []
    for digit_str in digits_string.split(' '):
        sorted_digit_str = sort_str(digit_str)
        result.append(signal_mapping[sorted_digit_str])

    result_str = ''
    for i in result:
        result_str = result_str + str(i)

    return int(result_str)
    
total_result = 0
for inp in parsed_input:
    signal_messages = inp[0]
    signal_digits = inp[1]
    signal_mapping = get_mapping(signal_messages)
    result = decode_string_to_digits(signal_mapping,signal_digits)
    total_result = total_result + result

print(total_result)
