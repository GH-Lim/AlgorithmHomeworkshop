import sys
sys.stdin = open('input.txt', 'r')


def dfs(v):
    global top
    if not visited[v]:
        visited[v] = True
        for pre in G[v]:
            if not visited[pre]:
                dfs(pre)
        top += 1
        result[top] = v


for tc in range(1, 11):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))
    # dp = [edges[2 * _] for _ in range(E)]
    # sp = [_ for _ in range(1, V+1) if _ not in dp]
    G = [[] for _ in range(V+1)]
    for i in range(E):
        G[edges[2 * i + 1]].append(edges[2 * i])
    visited = [False] * (V+1)
    result = [0] * V
    top = -1
    for i in range(1, V+1):
        dfs(i)
    print('#{} {}'.format(tc, ' '.join(map(str, result))))

#
# def dfs_2(v):
#     if not visited2[v] and not H[v]:
#         visited2[v] = True
#         result2.append(v)
#         for trail in G[v]:
#             H[trail].remove(v)
#             if not visited2[trail] and not H[trail]:
#                 dfs_2(trail)
#
#
# for tc in range(1, 11):
#     V, E = map(int, input().split())
#     edges = list(map(int, input().split()))
#     dp = [edges[2 * _ + 1] for _ in range(E)]
#     sp = [_ for _ in range(1, V+1) if _ not in dp]
#     G = [[] for _ in range(V+1)]
#     H = [[] for _ in range(V+1)]
#     for i in range(E):
#         G[edges[2 * i]].append(edges[2 * i + 1])
#         H[edges[2 * i + 1]].append(edges[2 * i])
#     visited2 = [False] * (V + 1)
#     result2 = []
#     for i in range(1, V+1):
#         dfs_2(i)
#     print('#{} {}'.format(tc, ' '.join(map(str, result2))))

#
# def dfs_3(v):
#     while len(result3) < V:
#
#
#
#
# for tc in range(1, 11):
#     V, E = map(int, input().split())
#     edges = list(map(int, input().split()))
#     dp = [edges[2 * _ + 1] for _ in range(E)]
#     sp = [_ for _ in range(1, V+1) if _ not in dp]
#     result3 = []
#     G = [[] for _ in range(V + 1)]
#     for i in range(E):
#         G[edges[2 * i]].append(edges[2 * i + 1])
#
#     print('#{} {}'.format(tc, ' '.join(map(str, result3))))
