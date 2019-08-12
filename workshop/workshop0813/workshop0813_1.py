import sys
sys.stdin = open('input_1.txt', 'r')


def palindrome(target, n):
    for k in range(100 - n + 1):
        j = 0
        i = 0
        while i < n//2:



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