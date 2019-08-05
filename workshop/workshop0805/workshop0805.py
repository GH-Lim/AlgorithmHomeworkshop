import sys
sys.stdin = open('input.txt', 'r')

for t in range(10):
    tc = int(input())
    arrays = []
    for r in range(100):
        row = list(map(int, input().split()))
        arrays.append(row)
    max_sum = 0
    sum_cross_1 = 0
    sum_cross_2 = 0
    for i in range(100):
        sum_row = 0
        sum_col = 0
        sum_cross_1 += arrays[i][i]
        sum_cross_2 += arrays[99 - i][i]
        for j in range(100):
            sum_row += arrays[i][j]
            sum_col += arrays[j][i]
        large = sum_row if sum_row > sum_col else sum_col
        max_sum = large if large > max_sum else max_sum

    large = sum_cross_1 if sum_cross_1 > sum_cross_2 else sum_cross_2
    max_sum = large if large > max_sum else max_sum

    print('#{} {}'.format(tc, max_sum))
