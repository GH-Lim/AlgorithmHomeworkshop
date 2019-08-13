import sys
sys.stdin = open('input_1.txt', 'r')


def palindrome(target, n):
    for i in range(100):
        for j in range(100 - n + 1):
            k = 0
            palin_row = True
            palin_col = True
            while 1:
                if palin_row:
                    if target[i][j + k] != target[i][j + n - 1 - k]:
                        palin_row = False
                if palin_col:
                    if target[j + k][i] != target[j + n - 1 - k][i]:
                        palin_col = False
                if palin_row or palin_col:
                    k += 1
                else:
                    break
                if k == n//2:
                    return True
    return False


arr = [[] for _ in range(100)]
for _ in range(10):
    tc = int(input())
    for i in range(100):
        arr[i] = list(map(str, input()))
    # print(arr)
    max_len = 0
    for n in range(100, 0, -1):
        if palindrome(arr, n):
            max_len = n
            break
    print(max_len)