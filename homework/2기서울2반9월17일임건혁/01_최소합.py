def dfs(i, j, s):
    global min_s
    if i == j == N - 1:
        min_s = min_s if min_s < s else s
        return
    if s > min_s:
        return
    if i + 1 < N:
        dfs(i + 1, j, s + arr[i + 1][j])
    if j + 1 < N:
        dfs(i, j + 1, s + arr[i][j + 1])


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_s = 999999
    dfs(0, 0, arr[0][0])

    print('#%d %d' % (tc, min_s))
