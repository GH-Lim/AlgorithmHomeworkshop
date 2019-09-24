import sys
sys.stdin = open('input.txt', 'r')


def Person_work(E, p):
    global max_E
    if E < max_E:
        return
    if p == N - 1:
        max_E = max_E if max_E > E else E
        return
    for i in range(N):
        if not visited[i] and P[p + 1][i]:
            visited[i] = 1
            Person_work(E * P[p + 1][i] / 100, p + 1)
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_E = 0
    Person_work(100, -1)
    print('#%d %.6f' % (tc, max_E))
