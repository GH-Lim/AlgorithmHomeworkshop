factorial = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
exp = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]


def measure(l, r, n):
    global ans
    if n == N:
        ans += 1
        return
    if l >= sum_w - l:
        ans += factorial[N - n] * exp[N - n]
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            measure(l + weights[i], r, n + 1)
            if r + weights[i] <= l:
                measure(l, r + weights[i], n + 1)
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    weights = list(map(int, input().split()))
    sum_w = sum(weights)
    visited = [0] * N
    ans = 0
    measure(0, 0, 0)
    print('#%d %d' % (tc, ans))


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


# # 틀린 코드
# from itertools import permutations
#
# def factorial(num):
#     r = 1
#     for i in range(2, num + 1):
#         r *= i
#     return r
# def measure(l, r, n):
#     global ans
#     if n == N - 1:
#         ans += 1
#         return
#     if l >= sum(weights) - l:
#         ans += factorial(N - n - 1) * (2 ** (N - n - 1))
#         return
#     measure(l + weights[perm[n + 1]], r, n + 1)
#     if r + weights[perm[n + 1]] <= l:
#         measure(l, r + weights[perm[n + 1]], n + 1)
#
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     perms = list(permutations(range(N)))
#     weights = list(map(int, input().split()))
#     visited = [0] * N
#     ans = 0
#     for perm in perms:
#         measure(0 + weights[perm[0]], 0, 0)
#     print('#%d %d' % (tc, ans))


# 시간초과
factorial = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
exp = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]


def measure(l, r, n):
    global ans
    if n == N:
        ans += 1
        return
    if l >= sum_w - l:
        ans += factorial[N - n] * exp[N - n]
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            measure(l + weights[i], r, n + 1)
            if r + weights[i] <= l:
                measure(l, r + weights[i], n + 1)
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    weights = list(map(int, input().split()))
    sum_w = sum(weights)
    visited = [0] * N
    ans = 0
    measure(0, 0, 0)
    print('#%d %d' % (tc, ans))


# def factorial(num):
#     r = 1
#     for i in range(2, num + 1):
#         r *= i
#     return r
#
#
# def measure(l, r, n):
#     global ans
#     if n == N:
#         # ans += 1
#         return 1
#     if l >= sum(weights) - l:
#         # ans += factorial(N - n) * 2 ** (N - n)
#         return factorial(N - n) * 2 ** (N - n)
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = 1
#             ans += measure(l + weights[i], r, n + 1)
#             if r + weights[i] <= l:
#                 ans += measure(l, r + weights[i], n + 1)
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
