# from collections import deque
import heapq
# heapq 모듈을 이용한 이진힙 구현
for tc in range(1, int(input()) + 1):
    N = int(input())
    nodes = list(map(int, input().split()))
    heap = []
    for i in range(N):
        heapq.heappush(heap, nodes[i])
    ans = 0
    while N != 1:
        N //= 2
        ans += heap[N - 1]
    print('#%d %d' % (tc, ans))


# # deque(양방향큐) 를 이용한 이진힙
# def change(k):
#     c = k
#     while nodes[P[c]] > nodes[c] and nodes[P[c]] != 0:
#         nodes[P[c]], nodes[c] = nodes[c], nodes[P[c]]
#         c = P[c]
#
#
# def ans(k):
#     c = k
#     result = 0
#     while P[c] != 0:
#         result += nodes[P[c]]
#         c = P[c]
#     return result
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     nodes = [0] + list(map(int, input().split()))
#     P = [0 for _ in range(N+1)]
#     queue = deque(range(2, N+1))
#     for i in range(1, N//2 + 1):
#         if queue:
#             temp = queue.popleft()
#             P[temp] = i
#             change(temp)
#         if queue:
#             temp = queue.popleft()
#             P[temp] = i
#             change(temp)
#     print('#{} {}'.format(tc, ans(N)))
