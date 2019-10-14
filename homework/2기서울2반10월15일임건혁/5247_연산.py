from collections import deque


def ans(n):
    q = deque()
    q.append(n)
    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):
            num = q.popleft()
            for i in range(4):
                res = calc(num, i)
                if res == M:
                    break
                if res not in visited and 0 < res <= 1000000:
                    visited[res] = 1
                    q.append(res)
            else:
                continue
            break
        else:
            continue
        break
    return cnt


def calc(num, op):
    if op == 0:
        return num + 1
    elif op == 1:
        return num - 1
    elif op == 2:
        return num * 2
    else:
        return num - 10


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    visited = {}
    print('#%d %d' % (tc, ans(N)))
