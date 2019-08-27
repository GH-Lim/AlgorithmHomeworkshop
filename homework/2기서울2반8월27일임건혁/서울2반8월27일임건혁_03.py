import sys
sys.stdin = open('03.txt', 'r')


def rcp(a, b):
    if cards[a] == 1:
        if cards[b] == 2:
            return b
        else:
            return a
    elif cards[a] == 2:
        if cards[b] == 3:
            return b
        else:
            return a
    else:
        if cards[b] == 1:
            return b
        else:
            return a


def div(i, j):
    # if i == j:
    #     return i
    if j - i <= 1:
        return rcp(i, j)
    left_group = div(i, (i + j) // 2)
    right_group = div((i + j) // 2 + 1, j)
    return rcp(left_group, right_group)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    print('#{} {}'.format(tc, div(0, N-1)+1))
