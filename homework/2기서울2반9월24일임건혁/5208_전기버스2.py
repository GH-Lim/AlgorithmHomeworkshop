def bus(n, cnt):
    global min_cnt
    if n >= N[0]:
        min_cnt = min(min_cnt, cnt)
        return
    for i in range(N[n], 0, -1):
        if cnt + 1 < min_cnt:
            bus(n + i, cnt + 1)


for tc in range(1, int(input()) + 1):
    N = list(map(int, input().split()))
    min_cnt = N[0]
    bus(1, -1)
    print('#%d %d' % (tc, min_cnt))
