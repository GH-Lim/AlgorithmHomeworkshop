import sys

sys.stdin = open('input.txt', 'r')
def buble_sort(nums, n):
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

def sum_heights(h):
    sum_h = 0
    for i in range(100):
        sum_h += h[i]
    return sum_h

T = 10

for tc in range(1, T+1):
    dumps = int(input())
    heights = list(map(int, input().split()))
    sort_h = buble_sort(heights, 100)
    s = sum_heights(heights)

    print(sort_h, heights, s)
    # print('#{0} {1}'.format(tc, result))
