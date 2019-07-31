import sys

sys.stdin = open('input.txt', 'r')
def counting(nums):
    c = [0] * 100
    for i in range(100):
        for j in range(100):
            if i+1 == nums[j]:
                c[i] += 1
    return c
def sum_heights(h):
    sum_h = 0
    for i in range(100):
        sum_h += h[i]
    return sum_h
def max_H(c):
    for i in range(99, 0, -1):
        if c[i] != 0:
            return i
def min_H(c):
    for i in range(100):
        if c[i] != 0:
            return i

T = 10

for tc in range(1, T+1):
    dumps = int(input())
    heights = list(map(int, input().split()))
    c = counting(heights)
    s = sum_heights(heights)

    max_h = max_H(c)
    min_h = min_H(c)

    for i in range(dumps):
        if c[max_h] == 0:
            max_h -= 1
        if c[min_h] == 0:
            min_h += 1

        if s % 100 == 0 and max_h - min_h == 0:
            break
        elif s % 100 != 0 and max_h - min_h == 1:
            break

        c[max_h] -= 1
        c[max_h-1] += 1
        c[min_h] -= 1
        c[min_h+1] += 1

    result = max_H(c) - min_H(c)
    print('#{0} {1}'.format(tc, result))
