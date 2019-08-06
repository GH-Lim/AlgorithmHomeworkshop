T = int(input())
A = list(range(1, 13))
n = len(A)


def my_sum(arr):
    result = 0
    for i in range(len(arr)):
        result += arr[i]
    return result


def my_append(arr, element):
    arr += [element]


for tc in range(1, T+1):
    N, K = map(int, input().split())
    count = 0
    for i in range(1 << n):
        a = []
        for j in range(n + 1):
            if i & (1 << j):
                my_append(a, A[j])
        if len(a) == N:
            if my_sum(a) == K:
                count += 1
    print('#{} {}'.format(tc, count))
