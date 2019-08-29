# import sys
# sys.stdin = open('04.txt', 'r')


def my_perm(k, sum_arr):
    global result
    if sum_arr > result:
        return
    if k == N:
        result = min(result, sum_arr)
        return
    for i in range(N):
        if visit[i] == 1:
            continue
        visit[i] = 1
        my_perm(k + 1, sum_arr + arr[k][i])
        visit[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0 for _ in range(N)]
    result = 999
    my_perm(0, 0)

    print("#{} {}".format(tc, result))
