def dfs(n):
    for i in L[n]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    r = list(map(int, input().split()))
    L = [[] for _ in range(N + 1)]
    for i in range(M):
        L[r[2 * i]].append(r[2 * i + 1])
        L[r[2 * i + 1]].append(r[2 * i])
    cnt = 0
    visited = [0] * (N + 1)
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = 1
            dfs(i)
            cnt += 1
    print('#%d %d' % (tc, cnt))
