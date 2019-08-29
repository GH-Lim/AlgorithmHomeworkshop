import sys
sys.stdin = open('04.txt', 'r')
from collections import deque


def bfs(s, d):
    queue = deque()
    visited = [0] * (V + 1)
    visited[s] = 1
    queue.append(s)
    step = 0
    while queue:
        step += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if G[node][d] == 1:
                return step
            for i in range(1, V + 1):
                if G[node][i] and not visited[i]:
                    visited[i] = 1
                    queue.append(i)
    return 0


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    G = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        G[v1][v2] = 1
        G[v2][v1] = 1
    S, D = map(int, input().split())
    print('#{} {}'.format(tc, bfs(S, D)))
