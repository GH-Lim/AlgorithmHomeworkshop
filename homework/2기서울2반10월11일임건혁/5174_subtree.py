T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    L = [[] for _ in range(E + 2)]
    for i in range(E):
        L[edges[2*i]].append(edges[2*i + 1])
    stack = [N]
    cnt = 0
    while stack:
        node = stack.pop()
        cnt += len(L[node])
        stack += L[node]
    cnt += 1
    print('#{} {}'.format(tc, cnt))
