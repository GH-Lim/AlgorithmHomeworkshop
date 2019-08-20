def dfs(s):
    visited[s] = 1
    for w in L[s]:
        if not visited[w]:
            dfs(w)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    L = [[] for _ in range(V + 1)]
    for _ in range(E):
        sp, dp = map(int, input().split())
        L[sp].append(dp)
    S, G = map(int, input().split())
    visited = [0] * (V+1)
    dfs(S)

    print('#{} {}'.format(tc, visited[G]))
