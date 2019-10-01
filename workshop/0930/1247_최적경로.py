def solve(next_node, step, distance):
    global ans
    if step == N:
        ans = min(ans, distance + G[next_node][1])
        return
    for i in range(2, N + 2):
        if not visited[i] and distance + G[next_node][i] < ans:
            visited[i] = 1
            solve(i, step + 1, distance + G[next_node][i])
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    points = list(map(int, input().split()))

    G = [[] for _ in range(N + 2)]
    for i in range(N + 2):
        G[i] = [abs(points[2*i] - points[2*j]) + abs(points[2*i + 1] - points[2*j + 1]) for j in range(N + 2)]
    visited = [0] * (N + 2)
    ans = 999999
    for i in range(2, N + 2):
        visited[i] = 1
        solve(i, 1, G[0][i])
        visited[i] = 0
    print('#%d %d' % (tc, ans))
