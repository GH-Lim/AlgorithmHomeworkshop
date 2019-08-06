T = int(input())


def binary_search(arr, target):
    count = 0
    l = arr[0]
    r = arr[-1]
    while l <= r:
        c = int((l + r) / 2)
        count += 1
        if c == target:
            return count
        elif c > target:
            r = c
        else:
            l = c
    return arr[-1]


for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    pages = list(range(1, P+1))

    A = binary_search(pages, Pa)
    B = binary_search(pages, Pb)

    if A == B:
        win = 0
    elif A < B:
        win = 'A'
    else:
        win = 'B'
    print('#{} {}'.format(tc, win))
