def in_order(node):
    l, r = L[node]
    if l:
        in_order(l)
    print(nodes[node], end='')
    if r:
        in_order(r)


for tc in range(1, 11):
    N = int(input())
    nodes = ['0'] * (N + 1)
    L = [[0, 0] for _ in range(N + 1)]
    for i in range(1, N + 1):
        info = input().split()
        l, r = 0, 0
        if len(info) > 2:
            l = int(info[2])
            if len(info) == 4:
                r = int(info[3])
        nodes[i] = info[1]
        L[i][0], L[i][1] = l, r
    print('#%d ' % tc, end='')
    in_order(1)
    print()
