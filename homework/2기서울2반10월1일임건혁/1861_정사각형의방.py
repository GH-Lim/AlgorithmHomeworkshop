# bfs?
def calc(y, x):
    global ans_cnt, ans_room
    room_val[y][x] = 1
    q = list()
    q.append((y, x))
    while q:
        yy, xx = q.pop()
        for d in range(4):
            ny, nx = yy + dy[d], xx + dx[d]
            if 0 <= ny < N and 0 <= nx < N and rooms[ny][nx] - rooms[yy][xx] == 1:
                if not room_val[ny][nx]:
                    q.append((ny, nx))
                    room_val[ny][nx] = 1
                    room_val[y][x] += 1
                else:
                    room_val[y][x] += room_val[ny][nx]

    if ans_cnt < room_val[y][x]:
        ans_cnt = room_val[y][x]
        ans_room = rooms[y][x]
    elif ans_cnt == room_val[y][x]:
        ans_room = min(ans_room, rooms[y][x])


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for tc in range(1, int(input()) + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    room_val = [[0] * N for _ in range(N)]
    ans_room = N
    ans_cnt = 0

    for i in range(N):
        for j in range(N):
            if not room_val[i][j]:
                calc(i, j)
    print('#%d %d %d' % (tc, ans_room, ans_cnt))


# # 재귀 속도 느리고 최대 깊이 초과
# from sys import setrecursionlimit
# setrecursionlimit(10000)
#
#
# def dfs(y, x, cnt):
#     global ans_room
#     global ans_cnt
#     if ans_cnt < cnt:
#         ans_room = room
#         ans_cnt = cnt
#     elif ans_cnt == cnt:
#         ans_room = min(ans_room, room)
#     for d in range(4):
#         ny, nx = y + dy[d], x + dx[d]
#         if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and rooms[ny][nx] - rooms[y][x] == 1:
#             visited[ny][nx] = 1
#             dfs(ny, nx, cnt + 1)
#             visited[ny][nx] = 0
#
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     rooms = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     ans_room = N
#     ans_cnt = 0
#     for i in range(N):
#         for j in range(N):
#             room = rooms[i][j]
#             visited[i][j] = 1
#             dfs(i, j, 1)
#             visited[i][j] = 0
#     print('#%d %d %d' % (tc, ans_room, ans_cnt))


# # DP 실패
# def calc(y, x):
#     for d in range(4):
#         ny, nx = y + dy[d], x + dx[d]
#         if 0 <= ny < N and 0 <= nx < N and rooms[ny][nx] - rooms[y][x] == 1:
#             if not visited[ny][nx]:
#                 calc(ny, nx)
#             return 1 + calc(ny, nx)
#     else:
#         visited[y][x] = 1
#         room_val[y][x] = 1
#         return
#
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     rooms = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     room_val = [[0] * N for _ in range(N)]
#     ans_room = N
#     ans_cnt = 0
#
#     for i in range(N):
#         for j in range(N):
#             if not visited[i][j]:
#                 room_val[i][j] = calc(i, j)
#     for row in room_val:
#         print(row)


# # 어색한 DP
# def calc(y, x):
#     global ans_cnt, ans_room
#     for d in range(4):
#         ny, nx = y + dy[d], x + dx[d]
#         if 0 <= ny < N and 0 <= nx < N and rooms[ny][nx] - rooms[y][x] == 1:
#             if not visited[ny][nx]:
#                 visited[y][x] = 1
#                 calc(ny, nx)
#                 room_val[y][x] = 1 + room_val[ny][nx]
#                 break
#             else:
#                 visited[y][x] = 1
#                 room_val[y][x] = 1 + room_val[ny][nx]
#                 break
#     else:
#         visited[y][x] = 1
#         room_val[y][x] = 1
#     if ans_cnt < room_val[i][j]:
#         ans_cnt = room_val[i][j]
#         ans_room = rooms[i][j]
#     elif ans_cnt == room_val[i][j]:
#         ans_room = min(ans_room, rooms[i][j])
#
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     rooms = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     room_val = [[0] * N for _ in range(N)]
#     ans_room = N
#     ans_cnt = 0
#
#     for i in range(N):
#         for j in range(N):
#             if not visited[i][j]:
#                 calc(i, j)
#     print('#%d %d %d' % (tc, ans_room, ans_cnt))


