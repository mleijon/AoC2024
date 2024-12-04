def safe(rep) -> bool:
    if not(all(x > 0 for x in rep) or all(x < 0 for x in rep)):
        return False
    if all((3 >= x >= 1)  or (-1 >= x >= -3) for x in rep):
        return True
    else:
        return False
def diffs(rep) -> list:
    return [rep[1:][x] - rep[:len(rep)][x] for x in list(range(len(rep) - 1))]


if __name__ == '__main__':
    with open("d2_input.txt") as f:
        count_1 = 0
        count_2 = 0
        for row in f:
            report = [int(x) for x in row.split()]
            test = diffs(report)
            safe_rep = safe(test)
            count_1 += safe_rep
            if safe_rep:
                count_2 += safe_rep
            else:
                for i in range(len(report)):
                    short_report = report.copy()
                    del short_report[i]
                    test = diffs(short_report)
                    if safe(test):
                        count_2 += 1
                        break
        print('The answer to part 1 is: {}'.format(count_1))
        print('The answer to part 2 is: {}'.format(count_2))


