T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = []
    for _ in range(M):
        nums = input().split()
        if not result:
            result += nums
        else:
            idx = -1
            for i in range(len(result)):
                if int(nums[0]) < int(result[i]):
                    idx = i
                    break
            if idx == -1:
                result += nums
            else:
                result[idx:0] = nums
    print('#{} {}'.format(tc, ' '.join(result[-1:-11:-1])))
