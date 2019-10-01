# # 시간초과
# def measure(l, r, n):
#     global ans
#     if n == N:
#         ans += 1
#         return
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = 1
#             if r + weights[i] <= l:
#                 measure(l, r + weights[i], n + 1)
#             measure(l + weights[i], r, n + 1)
#             visited[i] = 0
#
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     weights = list(map(int, input().split()))
#     visited = [0] * N
#     ans = 0
#     measure(0, 0, 0)
#     print('#%d %d' % (tc, ans))


# 시간초과
from itertools import permutations
def measure(l, r, n, p):
    global ans
    if n == N - 1:
        ans += 1
        return
    if r + p[n + 1] <= l:
        measure(l, r + p[n + 1], n + 1, p)
    measure(l + p[n + 1], r, n + 1, p)


for tc in range(1, int(input()) + 1):
    N = int(input())
    perms = list(permutations(range(N)))
    # print(perms)
    weights = list(map(int, input().split()))
    visited = [0] * N
    ans = 0
    for perm in perms:
        measure(0 + perm[0], 0, 0, perm)
    print('#%d %d' % (tc, ans))



# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     weights = list(map(int, input().split()))
#     visited = [0] * N
#     ans = 0
#     print('#%d %d' % (tc, ans))
