from collections import Counter
l1 = []
l2 = []

with open("input.txt") as f:
    for row in f:
        l1.append(int(row.split()[0]))
        l2.append(int(row.split()[1]))
l1.sort()
l2.sort()
print('The answer to part 1 is: {}'.format(sum([abs(x - y) for x,y in zip(l1, l2)])))

similarity_score = 0
cnt_l1 = Counter()
cnt_l2 = Counter()
for item in l1:
    cnt_l1[item] += 1
for item in l2:
    cnt_l2[item] += 1
for item in cnt_l1.keys():
    similarity_score += item*cnt_l1[item]*cnt_l2[item]
print('The answer to part 2 is: {}'.format(similarity_score))
