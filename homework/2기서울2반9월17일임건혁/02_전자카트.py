def move(s, p, depth):
    global min_P
    if p >= min_P:
        return
    if depth == N - 1:
        p += G[s][0]
        min_P = min_P if min_P < p else p
        return
    for i in range(1, N):
        if not visited[i]:
            visited[i] = 1
            move(i, p + G[s][i], depth + 1)
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_P = 999999
    move(0, 0, 0)
    print('#%d %d' % (tc, min_P))
