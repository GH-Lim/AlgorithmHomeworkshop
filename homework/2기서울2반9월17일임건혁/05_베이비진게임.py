from collections import deque
for tc in range(1, int(input()) + 1):
    cards = deque(map(int, input().split()))
    A = []
    B = []
    result = 0
    for i in range(6):
        if i > 1:
            A.append(cards.popleft())
            A.sort()
            for a in range(i - 1):
                if A[a] == A[a + 1] == A[a + 2]:
                    result = 1
                    break
            if not result:
                a = 0
                cnt = 0
                while a < i:
                    if A[a + 1] - A[a] == 1:
                        cnt += 1
                        a += 1
                    elif A[a + 1] - A[a] == 0:
                        a += 1
                    else:
                        a += 1
                        cnt = 0
                    if cnt == 2:
                        result = 1
                        break
            if result:
                break
            B.append(cards.popleft())
            B.sort()
            for b in range(i - 1):
                if B[b] == B[b + 1] == B[b + 2]:
                    result = 2
                    break
                if not result:
                    b = 0
                    cnt = 0
                    while b < i:
                        if B[b + 1] - B[b] == 1:
                            cnt += 1
                            b += 1
                        elif B[b + 1] - B[b] == 0:
                            b += 1
                        else:
                            b += 1
                            cnt = 0
                        if cnt == 2:
                            result = 2
                            break
            if result:
                break
        else:
            A.append(cards.popleft())
            B.append(cards.popleft())
    print('#%d %d' % (tc, result))
