T = int(input())

def sum_M(nums, n, M):
    sum_m = 0
    for i in range(M):
        sum_m += nums[n+i]
    return sum_m
def buble_sort(nums, n):
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

for case in range(1, T+1):

    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    sum_nums = [0] * (N-M+1)

    for i in range(N-M+1):
        sum_nums[i] = sum_M(numbers, i, M)

    buble_sort(sum_nums, N-M+1)
    max_M = sum_nums[-1]
    min_M = sum_nums[0]
    max_sub_min = max_M - min_M
    print('#{0} {1}'.format(case, max_sub_min))
