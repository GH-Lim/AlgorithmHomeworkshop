for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    L = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)

    for _ in range(M):
        a, b = map(int, input().split())
        L[a].append(b)
        L[b].append(a)
    q = []
    visited[1] = 1
    cnt = 0
    for a in L[1]:
        visited[a] = 1
        q.append(a)
        cnt += 1
    while q:
        a = q.pop()
        for b in L[a]:
            if not visited[b]:
                cnt += 1
                visited[b] = 1

    print('#%d %d' % (tc, cnt))
