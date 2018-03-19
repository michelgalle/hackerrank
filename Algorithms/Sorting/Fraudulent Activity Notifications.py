import sys
from bisect import bisect_left, insort_left


def activityNotifications(expenditure, d):
    """ Worst-case: O( n ) """

    frauds = 0
    wind = sorted(expenditure[:d])
    wbisect = bisect_left
    winsort = insort_left
    half = d // 2
    left_half = half - 1

    if d % 2 != 0:
        for i, val in enumerate(expenditure[d:]):
            if val >= 2 * wind[half]:
                frauds += 1
            del wind[wbisect(wind, expenditure[i])]
            winsort(wind, val)
    else:
        for i, val in enumerate(expenditure[d:]):
            if val >= (wind[half] + wind[left_half]):
                frauds += 1
            del wind[wbisect(wind, expenditure[i])]
            winsort(wind, val)

    return frauds


if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    expenditure = list(map(int, input().strip().split(' ')))
    result = activityNotifications(expenditure, d)
    print(result)
