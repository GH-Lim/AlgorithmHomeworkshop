import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']


def counting_sort(target_arr, sort_arr, target_len):
    C = [0] * 10

    for i in range(target_len):
        for j in range(10):
            if target_arr[i] == nums[j]:
                C[j] += 1
                break
    for i in range(1, 10):
        C[i] += C[i-1]
    for i in range(target_len-1, -1, -1):
        for j in range(10):
            if target_arr[i] == nums[j]:
                sort_arr[C[j]-1] = target_arr[i]
                C[j] -= 1


for t in range(T):
    tc_num, tc_len = input().split()
    tc = input().split()
    result = [0] * int(tc_len)

    counting_sort(tc, result, int(tc_len))

    print(tc_num)
    print(' '.join(result))
