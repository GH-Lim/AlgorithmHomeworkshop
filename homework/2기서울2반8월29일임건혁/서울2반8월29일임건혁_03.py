import sys
sys.stdin = open('03.txt', 'r')
from collections import deque
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    chz = list(map(int, input().split()))
    pizza = deque([i + 1, chz[i]] for i in range(M))
    oven = deque()
    for i in range(N):
        oven.append(pizza.popleft())
    while pizza:
        check = oven.popleft()
        check[1] //= 2
        if check[1] == 0:
            oven.append(pizza.popleft())
        else:
            oven.append(check)
    while oven:
        check = oven.popleft()
        check[1] //= 2
        if check[1]:
            oven.append(check)
    print('#{} {}'.format(tc, check[0]))
