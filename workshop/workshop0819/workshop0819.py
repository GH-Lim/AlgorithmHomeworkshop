import sys
sys.stdin = open('input.txt', 'r')

for case in range(10):
    tc = input()

    data = [input().split() for _ in range(100)]

    for i in range(100):
        if data[99][i] == '2':
            c = i
            break
    r = 99
    dc = [-1, 0, 1]
    mode = 1

    while r > 0:
        if data[r - 1][c] == '1':
            if c < 99 and data[r][c + 1] == '1':
                if mode == 0:
                    mode = 1
                    r -= 1
                else:
                    mode = 2
                c += dc[mode]
            elif c > 0 and data[r][c - 1] == '1':
                if mode == 2:
                    mode = 1
                    r -= 1
                else:
                    mode = 0
                c += dc[mode]
            else:
                r -= 1
        else:
            c += dc[mode]

    print('#{} {}'.format(tc, c))