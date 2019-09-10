import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    checked = []
    sum_codes = 0
    codes = [bin(int(input(), 16))[2:].zfill(M * 4) for _ in range(N)]
    for i in range(N):
        for j in range(M * 4):
            checked.append((i,j))
    print(sum_codes)


