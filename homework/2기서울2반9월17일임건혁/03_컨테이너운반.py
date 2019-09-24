for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    w = sorted(list(map(int, input().split())))
    t = sorted(list(map(int, input().split())), reverse=True)

    total_w = 0
    for truck in t:
        while w:
            temp_w = w.pop()
            if temp_w <= truck:
                total_w += temp_w
                break
    print('#%d %d' % (tc, total_w))
