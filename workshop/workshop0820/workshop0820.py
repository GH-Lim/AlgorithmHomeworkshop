import sys
sys.stdin = open('input.txt', 'r')


def dfs(v):
    pass


for tc in range(1, 11):
    V, E = map(int, input().split())
    nodes = list(range(1, V + 1))
    edges = list(map(int, input().split()))

    G = [[0 for _ in range(V)] for _ in range(V)]
    for i in range(E // 2):

