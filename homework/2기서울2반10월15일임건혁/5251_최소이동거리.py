from queue import PriorityQueue

INF = 1e9
for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    L = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        L[s].append([w, e])
    visited = [0] * (N + 1)

    # Dijkstra
    dij_list = [INF] * (N + 1)
    pq = PriorityQueue()
    dij_list[0] = 0
    pq.put((0, 0))
    while True:
        cost, now = pq.get()
        if now == N:
            break
        visited[now] = 1
        for n_cost, next_ in L[now]:
            if not visited[next_]:
                if cost + n_cost < dij_list[next_]:
                    dij_list[next_] = cost + n_cost
                    pq.put((dij_list[next_], next_))
    print('#%d %d' % (tc, dij_list[N]))
