import sys
sys.stdin = open('input_0.txt', 'r')


def palindrome(target, n):
    count = 0
    for i in range(8):
        for j in range(8 - n + 1):
            k = 0
            palin_row = True
            palin_col = True
            while k < n//2:
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
                if k == n // 2:
                    if palin_col:
                        count += 1
                    if palin_row:
                        count += 1
    return count


arr = [0] * 8
for tc in range(1, 11):
    n = int(input())
    for i in range(8):
        arr[i] = input()
    result = palindrome(arr, n)
    print('#%d %d' % (tc, result))
