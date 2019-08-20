import sys
sys.stdin = open('input.txt', 'r')


def dfs(v):



for tc in range(1, 11):
    V, E = map(int, input().split())
    # nodes = list(range(V + 1))
    edges = list(map(int, input().split()))
    dp = [edges[2 * _ - 1] for _ in range(E)]
    sp = [_ for _ in range(1, V+1) if _ not in dp]
    G = [[] for _ in range(V+1)]
    for i in range(E):
        G[edges[2 * i]].append(edges[2 * i + 1])
    # print(G)

