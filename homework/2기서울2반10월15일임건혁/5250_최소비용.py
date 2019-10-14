from queue import PriorityQueue


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
INF = 1e9
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    costs = [[INF] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    costs[0][0] = 0
    pq = PriorityQueue()
    pq.put((0, 0, 0))
    while True:
        cost, y, x = pq.get()
        if y == N - 1 and x == N - 1:
            break
        visited[y][x] = 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                n_cost = 1
                if arr[ny][nx] > arr[y][x]:
                    n_cost += arr[ny][nx] - arr[y][x]
                if cost + n_cost < costs[ny][nx]:
                    costs[ny][nx] = cost + n_cost
                    pq.put((costs[ny][nx], ny, nx))
    print('#%d %d' % (tc, costs[N - 1][N - 1]))
