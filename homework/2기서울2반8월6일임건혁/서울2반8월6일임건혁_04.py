T = int(input())


def special_sort(arr):
    for i in range(len(arr)-1):
        if i % 2:
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        else:
            max_idx = i
            for j in range(i+1, len(arr)):
                if arr[max_idx] < arr[j]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]


for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    special_sort(nums)
    result_arr = [str(nums[i]) for i in range(10)]
    print('#{} {}'.format(tc, ' '.join(result_arr)))
