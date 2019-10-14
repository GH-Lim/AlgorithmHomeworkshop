from heapq import heappush, heappop


def prim(n):  # 시작 노드
    w_list = [INF] * (V + 1)
    w_list[n] = 0
    hq = [(0, n)]
    for _ in range(V - 1):  # V - 1 개의 간선을 뽑는다
        now_w, now = heappop(hq)
        visited[now] = 1
        for next_w, next_ in L[now]:
            if not visited[next_]:
                if w_list[next_] > next_w:
                    w_list[next_] = next_w
                    heappush(hq, (next_w, next_))
    return w_list


INF = 2e9
for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    L = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        L[n1].append([w, n2])
        L[n2].append([w, n1])
    visited = [0] * (V + 1)
    p_list = prim(0)
    print('#%d %d' % (tc, sum(p_list)))
