import sys
sys.stdin = open('input.txt', 'r')


def findchem(a, b):
    row = 1
    col = 1
    k = a
    l = b
    while k + 1 < N and arr[k + 1][b] != 0:
        k += 1
        row += 1
    while l + 1 < N and arr[a][l + 1] != 0:
        l += 1
        col += 1
    for i in range(a, k+1):
        for j in range(b, l+1):
            visited[i][j] = 1
    return [row * col, row, col]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    chem_infos = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and arr[i][j]:
                chem_infos.append(findchem(i, j))
    chem_infos.sort()
    print('#{} {}'.format(tc, len(chem_infos)), end='')
    for info in chem_infos:
        print(' {} {}'.format(info[1], info[2]), end='')
    print()
