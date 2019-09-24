def merge_sort(m):
    if len(m) == 1:
        return m
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    global cnt
    result = [0] * (len(left) + len(right))
    if left[-1] > right[-1]:
        cnt += 1
    i, j, k = 0, 0, 0
    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result[k] = left[i]
                i += 1
                k += 1
            else:
                result[k] = right[j]
                j += 1
                k += 1
        elif i < len(left):
            result[k:] = left[i:]
            break
        elif j < len(right):
            result[k:] = right[j:]
            break
    return result


for tc in range(1, int(input()) + 1):
    N = int(input())
    L = list(map(int, input().split()))
    cnt = 0
    print('#%d %d %d' % (tc, merge_sort(L)[N // 2], cnt))
