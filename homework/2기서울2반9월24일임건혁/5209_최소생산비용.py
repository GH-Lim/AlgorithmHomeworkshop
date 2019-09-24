def back_track(n, cost):
    global ans
    if n == N - 1:
        ans = min(ans, cost)
        return
    else:
        for i in range(N):
            if not visited[i] and ans > cost + arr[n + 1][i]:
                visited[i] = 1
                back_track(n + 1, cost + arr[n + 1][i])
                visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 99 * N
    visited = [0] * N
    back_track(-1, 0)
    print('#%d %d' % (tc, ans))
