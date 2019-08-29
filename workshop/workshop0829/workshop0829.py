import sys
sys.stdin = open('input.txt', 'r')
from pprint import pprint

from collections import deque


def call(G, v):
    visited = [0] * 101
    queue = deque()
    queue.append(v)
    while queue:
        t = queue.popleft()
        if not visited[t]
            visited[t] = True
            visit(t)


for tc in range(1, 11):
    L, start = map(int, input().split())
    edges = deque(map(int, input().split()))
    nodes = deque(deque() for _ in range(101))
    step = 0
    max_step = 0
    result = []
    while edges:
        temp_1 = edges.popleft()
        temp_2 = edges.popleft()
        if temp_2 not in nodes[temp_1]:
            nodes[temp_1].append(temp_2)
    # pprint(nodes)
    # print()
    call(start)
    print(result)
