import sys
sys.stdin = open('02.txt', 'r')

from collections import deque


def find_exit(i, j):
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 1
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    queue = deque()
    queue.append((i, j))
    step = 0
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            for mode in range(4):
                x = node[0] + dx[mode]; y = node[1] + dy[mode]
                if 0 <= x < N and 0 <= y < N:
                    if maze[x][y] == 0 and visited[x][y] == 0:
                        visited[x][y] = 1
                        queue.append((x, y))
                    if maze[x][y] == 3:
                        return step
        step += 1
    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        find = 0
        for j in range(N):
            if maze[i][j] == 2:
                sp = i, j
                find = 1
                break
        if find: break
    print('#{} {}'.format(tc, find_exit(*sp)))
