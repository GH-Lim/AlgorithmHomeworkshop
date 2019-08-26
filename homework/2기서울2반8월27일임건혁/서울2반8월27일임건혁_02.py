import sys
sys.stdin = open('02.txt', 'r')


def tracking(a, b):
    visited[a][b] = 1
    for vector in near:
        if 0 <= a + vector[0] < N and 0 <= b + vector[1] < N:
            if maze[a + vector[0]][b + vector[1]] == 0 and not visited[a + vector[0]][b + vector[1]]:
                if maze[a + vector[0]][b + vector[1]] == '3':
                    return 1
                stack.append((a + vector[0], b + vector[1]))
            while stack:
                next_v = stack.pop()
                tracking(next_v[0], next_v[1])
    return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    maze = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    stack = []
    near = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for j in range(N):
        if maze[N - 1][j] == '2':
            print(tracking(N - 1, j))
