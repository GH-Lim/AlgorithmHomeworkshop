from collections import deque
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    L = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        L[a].append(b)
        L[b].append(a)

    visited = [0] * (N + 1)
    ans = 0
    for i in range(1, N + 1):
        if not visited[i]:
            ans += 1
            visited[i] = 1
            q = deque()
            q.append(i)
            while q:
                j = q.popleft()
                for k in L[j]:
                    if not visited[k]:
                        visited[k] = 1
                        q.append(k)

    print('#%d %d' % (tc, ans))
