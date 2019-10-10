def in_order(node):
    l, r = L[node]
    if nodes[node] == '*':
        return in_order(l) * in_order(r)
    elif nodes[node] == '/':
        return in_order(l) / in_order(r)
    elif nodes[node] == '+':
        return in_order(l) + in_order(r)
    elif nodes[node] == '-':
        return in_order(l) - in_order(r)
    else:
        return nodes[node]


# def in_order_eval(node):
#     global ans
#     l, r = L[node]
#     if l:
#         ans += '('
#         in_order_eval(l)
#     ans += nodes[node]
#     if r:
#         in_order_eval(r)
#         ans += ')'


for tc in range(1, 11):
    N = int(input())
    nodes = [0] * (N + 1)
    L = [[0, 0] for _ in range(N + 1)]
    for i in range(1, N + 1):
        info = input().split()
        l, r = 0, 0
        if len(info) > 2:
            l = int(info[2])
            if len(info) == 4:
                r = int(info[3])
                nodes[i] = int(info[1])
        else:
            nodes[i] = info[1]
        L[i][0], L[i][1] = l, r
    print('#%d ' % tc, end='')
    print(int(in_order(1)))
    # ans = ''
    # in_order_eval(1)
    # print(int(eval(ans)))
