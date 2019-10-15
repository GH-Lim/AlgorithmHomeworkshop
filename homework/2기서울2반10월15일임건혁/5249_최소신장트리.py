# 프림 알고리즘
from heapq import heappush, heappop


def prim(n):  # 시작 노드
    w_list = [INF] * (V + 1)
    w_list[n] = 0
    hq = [(0, n)]
    for _ in range(V):  # V 개의 간선을 뽑는다
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


# # 크루스칼 알고리즘
# from queue import PriorityQueue
#
#
# def kruskal():
#     p = {}
#     rank = {}
#
#     def make_set(v):
#         p[v] = v
#         rank[v] = 0
#
#     def find_set(v):
#         if p[v] != v:
#             p[v] = find_set(p[v])
#         return p[v]
#
#     def union(v, u):
#         root1 = find_set(v)
#         root2 = find_set(u)
#         if rank[root1] > rank[root2]:
#             p[root2] = root1
#         else:
#             p[root1] = root2
#             if rank[root1] == rank[root2]:
#                 rank[root2] += 1
#
#     for v in range(V + 1):
#         make_set(v)
#
#     mst = []
#     while len(mst) != V:
#         w, v, u = edges.get()
#         if find_set(v) != find_set(u):
#             mst.append(w)
#             union(v, u)
#     return mst
#
#
# for tc in range(1, int(input()) + 1):
#     V, E = map(int, input().split())
#     edges = PriorityQueue()
#     for _ in range(E):
#         n1, n2, w = map(int, input().split())
#         if n2 > n1:
#             n1, n2 = n2, n1
#         edges.put([w, n1, n2])
#     k_list = kruskal()
#     print('#%d %d' % (tc, sum(k_list)))


# # 크루스칼 그냥 list
# def make_set(v):
#     p[v] = v
#     rank[v] = 0
#
#
# def find_set(v):
#     if p[v] != v:
#         p[v] = find_set(p[v])
#     return p[v]
#
#
# def union(v, u):
#     root1 = find_set(v)
#     root2 = find_set(u)
#     if rank[root1] > rank[root2]:
#         p[root2] = root1
#     else:
#         p[root1] = root2
#         if rank[root1] == rank[root2]:
#             rank[root2] += 1
#
#
# def kruskal():
#     for v in range(V + 1):
#         make_set(v)
#
#     mst = []
#     for edge in edges:
#         v, u, w = edge
#         if find_set(v) != find_set(u):
#             mst.append(w)
#             union(v, u)
#         if len(mst) == V:
#             break
#     return mst
#
#
# for tc in range(1, int(input()) + 1):
#     V, E = map(int, input().split())
#     edges = [list(map(int, input().split())) for _ in range(E)]
#     edges.sort(key=lambda x: x[2])
#     p = {}
#     rank = {}
#     k_list = kruskal()
#     print('#%d %d' % (tc, sum(k_list)))
