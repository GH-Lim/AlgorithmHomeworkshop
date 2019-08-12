import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for t in range(T):
    tc_num, tc_len = input().split()
    tc = input().split()

    c = [0] * 10

    for i in range(int(tc_len)):
        if tc[i][0] == 'Z':
            c[0] += 1
        elif tc[i][0] == 'O':
            c[1] += 1
        elif tc[i][0] == 'T':
            if tc[i][1] == 'W':
                c[2] += 1
            else:
                c[3] += 1
        elif tc[i][0] == 'F':
            if tc[i][1] == 'O':
                c[4] += 1
            else:
                c[5] += 1
        elif tc[i][0] == 'S':
            if tc[i][1] == 'I':
                c[6] += 1
            else:
                c[7] += 1
        elif tc[i][0] == 'E':
            c[8] += 1
        elif tc[i][0] == 'N':
            c[9] += 1
    print(tc_num)
    for i in range(10):
        for _ in range(c[i]):
            print(nums[i], end=' ')
    print()