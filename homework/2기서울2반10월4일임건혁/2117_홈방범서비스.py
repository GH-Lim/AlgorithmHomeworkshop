import sys
sys.stdin = open('2117.txt', 'r')

s_cost = [k ** 2 + (k - 1) ** 2 for k in range(1, 40)]
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    homes = [(i, j) for i in range(N) for j in range(N) if arr[i][j]]
    max_service = 0
    for i in range(N):
        for j in range(N):
            distances = [0] * 2 * N
            for home in homes:
                y, x = home
                distance = abs(y - i) + abs(x - j)
                distances[distance] += 1
            for k in range(2 * N):
                distances[k] += distances[k - 1]
                if s_cost[k - 1] <= distances[k - 1] * M and max_service < distances[k - 1]:
                    max_service = distances[k - 1]
    print('#%d %d' % (tc, max_service))
