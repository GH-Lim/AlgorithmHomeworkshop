def in_order(n):
    global k
    if n > N:
        return
    in_order(n * 2)
    nodes[n] = k
    k += 1
    in_order(n * 2 + 1)


for tc in range(1, int(input()) + 1):
    N = int(input())
    nodes = [0] * (N + 1)
    k = 1
    in_order(1)
    print('#%d %d %d' % (tc, nodes[1], nodes[N // 2]))


# # 첫 풀이
# from collections import deque
#
#
# def dfs(n):
#     global num
#     if L[n]:
#         dfs(L[n][0])
#         nodes[n] = num
#         num += 1
#         if len(L[n]) == 2:
#             dfs(L[n][1])
#     else:
#         nodes[n] = num
#         num += 1
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     L = [[] for _ in range(N+1)]
#     nodes = [0] * (N+1)
#     queue = deque(range(2, N+1))
#     num = 1
#     for i in range(1, N//2 + 1):
#         if queue:
#             L[i].append(queue.popleft())
#         if queue:
#             L[i].append(queue.popleft())
#     dfs(1)
#     print('#{} {} {}'.format(tc, nodes[1], nodes[N//2]))
