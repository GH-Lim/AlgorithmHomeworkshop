from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nodes = [0] + list(map(int, input().split()))
    L = [[] for _ in range(N+1)]
    P = [[] for _ in range(N+1)]
    queue = deque(range(2, N+1))
    num = 1
    for i in range(1, N//2 + 1):
        if queue:
            temp = queue.popleft()
            L[i].append(temp)
            P[temp].append(i)
        if queue:
            temp = queue.popleft()
            L[i].append(temp)
            P[temp].append(i)