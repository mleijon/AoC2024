import re
import numpy as np
word = "XMAS"
word_len = len(word)

def create_diags(in_list) -> list:
    out_list = list()
    length = len(in_list)
    for count in range(length):
        new_string1 = ""
        new_string2 = ""
        for row in range(count + 1):
            new_string1 += in_list[row][count - row]
            new_string2 += in_list[length - 1 - row][length - 1 - count + row]
        if word_len <= len(new_string1):
            out_list.append(new_string1)
        if length > len(new_string1) >= word_len:
            out_list.append(new_string1[::-1])
        if word_len <= len(new_string2):
            out_list.append(new_string2)
        if length > len(new_string2) >= word_len:
            out_list.append(new_string2[::-1])
    return out_list
    
rows_direct = list()
rows_reverse = list()
with open("d4_input.txt") as f:
    for row in f:
        rows_direct.append(row.strip())
        rows_reverse.append(row.strip()[::-1])
cols_direct = list(rows_direct[0])
cols_reverse = list()
for item in rows_direct[1:]:
    new_list = cols_direct.copy()
    for col_nr in range(len(cols_direct)):
       cols_direct[col_nr] = new_list[col_nr] + item[col_nr]
for item in cols_direct:
    cols_reverse.append(item[::-1])

diags_direct = create_diags(rows_direct)
diags_reverse = create_diags(rows_reverse)

sum_all = rows_direct + rows_reverse + cols_reverse + cols_direct + diags_direct + diags_reverse

sum = 0
for item in sum_all:
    sum += len(re.findall(word, item))

print('The answer to part 1 is: {}'.format(sum))

words = ["MMASS", "MSAMS", "SMASM", "SSAMM"]
with open("d4_input.txt") as f:
    puzzle = np.array([x for x in list(f.read()) if x != "\n"]).reshape(140, 140)
    it = np.nditer(puzzle, flags=['multi_index'])
    count = 0
    for pos in it:
        x = it.multi_index[0]
        y = it.multi_index[1]

        try:
            word = puzzle[x - 1, y - 1] + puzzle[x + 1, y - 1] + puzzle[x, y] + puzzle[x - 1, y + 1] + \
                   puzzle[x + 1, y + 1]
            if word in words:
                count += 1
        except:
            pass
print('The answer to part 2 is: {}'.format(count))



