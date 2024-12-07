import re

def calc_mults(m) -> int:
    sum = 0
    mults = re.findall(r"mul\([0-9]+,[0-9]+\)", m, re.MULTILINE)
    for mul in mults:
        sum += int(mul.split(',')[0][4:])*\
        int(mul.split(',')[1][:len(mul.split(',')[1]) - 1])
    return sum
with open("d3_input.txt") as f:
    memory = f.read()
print('The answer to part 1 is: {}'.format(calc_mults(memory)))
dont_split = memory.split('don\'t')
allowed_list = [dont_split[0]]
for item in dont_split:
    allowed_list.extend(item.split('do',1)[1:])
allowed = "".join(allowed_list)
print('The answer to part 2 is: {}'.format(calc_mults(allowed)))
