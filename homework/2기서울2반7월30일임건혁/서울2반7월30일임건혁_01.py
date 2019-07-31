T = int(input())

def buble_sort(nums, n):
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
for case in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    buble_sort(numbers, n)
    result = numbers[-1] - numbers[0]
    print('#{0} {1}'.format(case, result))
