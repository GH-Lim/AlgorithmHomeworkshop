def node(n):
    if n > N:
        return 0
    if nodes[n]:
        return nodes[n]
    l, r = n * 2, n * 2 + 1
    return node(l) + node(r)


for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    nodes = [0] * (N + 1)
    for _ in range(M):
        leaf, val = map(int, input().split())
        nodes[leaf] = val
    print('#%d %d' % (tc, node(L)))


# # 첫 풀이
# from collections import deque
#
#
# def dfs(k):
#     if C[k]:
#         for child in C[k]:
#             if nodes[child] == 0:
#                 dfs(child)
#             else:
#                 pass
#         for child in C[k]:
#             nodes[k] += nodes[child]
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M, L = map(int, input().split())
#     nodes = [0] * (N + 1)
#     C = [[] for _ in range(N + 1)]
#     q = deque(range(2, N + 1))
#     for _ in range(M):
#         n, v = map(int, input().split())
#         nodes[n] = v
#     for i in range(1, N//2 + 1):
#         if q:
#             temp = q.popleft()
#             C[i].append(temp)
#         if q:
#             temp = q.popleft()
#             C[i].append(temp)
#     dfs(1)
#     print('#{} {}'.format(tc, nodes[L]))
