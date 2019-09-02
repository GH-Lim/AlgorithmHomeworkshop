T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))
    for _ in range(M):
        nums.insert(*map(int, input().split()))
    print('#{} {}'.format(tc, nums[L]))
