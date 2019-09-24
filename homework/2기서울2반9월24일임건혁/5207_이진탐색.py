for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for b in B:
        low = 0
        high = N - 1
        flag = 0
        while low <= high:
            mid = low + (high - low) // 2

            if A[mid] == b:
                cnt += 1
                break
            elif A[mid] > b:
                if flag == -1:
                    break
                flag = -1
                high = mid - 1
            else:
                if flag == 1:
                    break
                flag = 1
                low = mid + 1
    print('#%d %d' % (tc, cnt))