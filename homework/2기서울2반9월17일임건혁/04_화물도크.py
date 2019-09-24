for tc in range(1, int(input()) + 1):
    N = int(input())
    S = []
    E = []
    for _ in range(N):
        s, e = map(int, input().split())
        if s in S:
            temp = S.index(s)
            if e < E[temp]:
                E[temp] = e
        else:
            S.append(s)
            E.append(e)
    apps = sorted(list(zip(E, S)))
    cnt = 0
    s = 0
    for app in apps:
        if app[1] >= s:
            cnt += 1
            s = app[0]
    print('#%d %d' % (tc, cnt))
