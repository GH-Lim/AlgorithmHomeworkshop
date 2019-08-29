import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
def call(s):
    visited = [0] * 101
    queue = deque()
    visited[s] = 1
    queue.append(s)
    while queue:
        result = 0
        for _ in range(len(queue)):
            t = queue.popleft()
            result = result if result > t else t
            for i in range(1, 101):
                if G[t][i] and not visited[i]:
                    visited[i] = 1
                    queue.append(i)
    return result


for tc in range(1, 11):
    L, start = map(int, input().split())
    edges = deque(map(int, input().split()))
    G = [[0] * 101 for _ in range(101)]
    while edges:
        temp_1 = edges.popleft()
        temp_2 = edges.popleft()
        G[temp_1][temp_2] = 1
    print('#{} {}'.format(tc, call(start)))
