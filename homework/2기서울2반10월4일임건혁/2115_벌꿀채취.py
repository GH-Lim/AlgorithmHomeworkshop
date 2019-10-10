# import sys
# sys.stdin = open('2115.txt', 'r')


def find_max(L):
    Max = L[0] ** 2
    for i in range(M - 1):
        for j in range(i + 1, M):
            k = j
            Sum = L[i]
            sub_max = L[i] ** 2
            while k < M:
                if Sum + L[k] <= C:
                    Sum += L[k]
                    sub_max += L[k] ** 2
                k += 1
            Max = max(Max, sub_max)
    return Max


for tc in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_arr = [[0] * N for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N - M + 1):
            select = sorted([arr[i][j + m] for m in range(M)], reverse=True)
            max_arr[i][j] = find_max(select)
    sub_arr = sum(max_arr, [])
    for i in range(N ** 2 - M):
        ans = max(ans, sub_arr[i] + max(sub_arr[i + M:]))
    print('#%d %d' % (tc, ans))


# def find_max(L):
#     Max = 0
#     for i in range(M - 1):
#         for j in range(i + 1, M):
#             k = j
#             Sum = L[i]
#             sub_max = L[i] ** 2
#             while k < M:
#                 if Sum + L[k] <= C:
#                     Sum += L[k]
#                     sub_max += L[k] ** 2
#                 k += 1
#             Max = max(Max, sub_max)
#     return Max
#
#
# def find_ans():
#     max_ = 0
#     for i in range(M - 1):
#         for j in range(i + 1, N):
#             iv, iy, ix = sub_arr[i]
#             jv, jy, jx = sub_arr[j]
#             if jy == iy and ix - M < jx < ix + M:
#                 continue
#             max_ = max(max_, iv + jv)
#     return max_
#
#
# for tc in range(1, int(input()) + 1):
#     N, M, C = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0
#     if M == 1:
#         sub_arr = sorted(sum(arr, []), reverse=True)
#         ans = sub_arr[0] ** 2 + sub_arr[1] ** 2
#     else:
#         max_arr = [[0] * (N - M + 1) for _ in range(N)]
#         for i in range(N):
#             for j in range(N - M + 1):
#                 select = sorted([arr[i][j + m] for m in range(M)], reverse=True)
#                 max_arr[i][j] = (find_max(select), i, j)
#         sub_arr = sorted(sum(max_arr, []), reverse=True)
#         ans = find_ans()
#     print('#%d %d' % (tc, ans))
