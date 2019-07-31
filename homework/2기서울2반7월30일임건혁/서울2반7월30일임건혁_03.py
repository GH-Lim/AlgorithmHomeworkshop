T = int(input())

def counting(nums, n):
    c = [0] * 10
    for i in range(10):
        for j in range(n):
            if i == nums[j]:
                c[i] += 1
    return c


for case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))
    
    max_count = 0
    max_num = 0
    counts = counting(numbers, N)

    for i in range(10):
        if max_count <= counts[i]:
            max_num = i
            max_count = counts[i] 
    
    print('#{0} {1} {2}'.format(case, max_num, max_count))
