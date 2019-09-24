def quick_sort(A, l, r):
    if l < r:
        s = Hoare_partition(A, l, r)
        quick_sort(A, l, s - 1)
        quick_sort(A, s + 1, r)


def Hoare_partition(A, l, r):
    p = A[l]
    i, j = l + 1, r
    while 1:
        while A[i] <= p and i < r:
            i += 1
        while A[j] >= p and j > l:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            break
    A[l], A[j] = A[j], A[l]
    return j


for tc in range(1, int(input()) + 1):
    N = int(input())
    L = list(map(int, input().split()))
    quick_sort(L, 0, N - 1)
    print('#%d %d' % (tc, L[N // 2]))
