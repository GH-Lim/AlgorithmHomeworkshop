import sys
sys.stdin = open('02.txt', 'r')

# def tracking(a, b):
#     global result
#     visited[a][b] = 1
#     for vector in near:
#         if not result:
#             if 0 <= a + vector[0] < N and 0 <= b + vector[1] < N and not visited[a + vector[0]][b + vector[1]]:
#                 if maze[a + vector[0]][b + vector[1]] == '0':
#                     tracking(a + vector[0], b + vector[1])
#                 elif maze[a + vector[0]][b + vector[1]] == '3':
#                     result = 1
#                     break
def is_ok(y, x):
    return 0<=y<N and 0<=x<N and maze[y][x] != '1'

def find_map(y, x):
    startY, startX = y, x
    global result
    if maze[startY][startX]=='3':
        result=1
        return
    visited.append((startY, startX))
    for vector in near:
        if not result and is_ok(startY + vector[0], startX + vector[1]):
            if (startY + vector[0], startX + vector[1]) not in visited:
                find_map(startY + vector[0], startX + vector[1])

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    maze = [list(input()) for _ in range(N)]
    # visited = [[0] * N for _ in range(N)]
    visited = []
    near = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                # tracking(i, j)
                find_map(i, j)
    print('#{} {}'.format(tc, result))
