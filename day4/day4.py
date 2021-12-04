def convert_string_to_matrix(string):
    result = []
    for line in string.split('\n'):
        if len(line) == 0:
            break
        row  = []
        for number in line.strip().split(' '):
            if len(number) != 0:
               row.append(int(number))
        result.append(row)
    return result


class Puzzle(object):
    def __init__(self,matrix):
        self.matrix = matrix 
        self.solved = False
        self.marked_numbers = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

    def mark_number(self,number):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if number == self.matrix[i][j]:
                    self.marked_numbers[i][j] = 1 
        solved,details = self.check_row_column_is_completed()
        print(self.marked_numbers,solved,number,details)
        rows_cols = None
        if details:
            rows_cols = self.get_details_row_or_column(details)
        return solved,rows_cols

    def get_details_row_or_column(self,details):
        if 'row' in details:
            row_no = details['row']
            row = self.matrix[row_no]
            return row
        if 'col' in details:
            col_no = details['col']
            col = []
            for i in range(len(self.matrix)):
                col.append(self.matrix[i][col_no])
            return col

    def check_row_column_is_completed(self):
        rows = [True for i in range(len(self.matrix))]
        cols = [True for j in range(len(self.matrix[0]))]
        for i in range(len(self.marked_numbers)):
            for j in range(len(self.marked_numbers[0])):
                if self.marked_numbers[i][j] == 0:
                    rows[i] = False
                    cols[j] = False
        for i,row in enumerate(rows):
            if row == True:
                return True,{'row':i}
        
        for j,col in enumerate(cols):
            if col == True:
                return True,{'col': j}
        return False,None

    def get_sum_unmarked(self):
        result = 0
        for i in range(len(self.marked_numbers)):
            for j in range(len(self.marked_numbers[0])):
                if self.marked_numbers[i][j] == 0:
                    result = result + self.matrix[i][j]
        return result

split_lines = open('day4.input').read().split("\n\n")
marked_numbers = split_lines[0]
matrix_strings = split_lines[1:]


# Solution for te first part 
"""
matrix_objects = []
for i in matrix_strings:
    matrix_objects.append(Puzzle(convert_string_to_matrix(i)))
result_found = False
result_matrix = None
result_details = None
result_number = -1
for i in marked_numbers.split(","):
    for matr in matrix_objects:
        result, details = matr.mark_number(int(i))
        if result == True:
            result_found = True
            result_matrix = matr
            result_details = details 
            result_number = int(i)
            break
    if result_found:
        break


matrix_unmarked_sum = matr.get_sum_unmarked()
solution_first = matrix_unmarked_sum*result_number
"""

# Solution for the second part 
matrix_objects = []
result_found = False
result_matrix = None 
result_details = None 
result_number = -1
for i in matrix_strings:
    matrix_objects.append(Puzzle(convert_string_to_matrix(i)))

matrixes_found = [False for i in range(len(matrix_objects))]

for no in marked_numbers.split(","):
    for index,matr in enumerate(matrix_objects):
        if matrixes_found[index] == True:
            continue
        result, details = matr.mark_number(int(no))
        if result == True:
            no_of_false = 0
            for found in matrixes_found:
                if not found:
                    no_of_false = no_of_false + 1
            if no_of_false > 1:
                matrixes_found[index] = True
            else:
                result_found = True
                result_matrix = matr 
                result_details = details 
                result_number = int(no)
    if result_found:
            break
        
matrix_unmarked_sum = result_matrix.get_sum_unmarked()
print(matrix_unmarked_sum*result_number)


