def dfs(y, x, num, step):
    if step == 7:
        visited[num] = 1
        return
    for v in range(4):
        ny = y + dy[v]
        nx = x + dx[v]
        if 0 <= ny < 4 and 0 <= nx < 4:
            dfs(ny, nx, num * 10 + arr[ny][nx], step + 1)


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    visited = {}
    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j], 1)
    print('#%d %d' % (tc, len(visited)))
