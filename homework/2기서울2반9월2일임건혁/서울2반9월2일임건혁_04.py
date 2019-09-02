T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    nums = input().split()

    for _ in range(M):
        command = input().split()

        if command[0] == 'D':
            del nums[int(command[1])]
        elif command[0] == 'I':
            nums.insert(int(command[1]), command[2])
        elif command[0] == 'C':
            nums[int(command[1])] = command[2]
    if len(nums) < L:
        print('#{} {}'.format(tc, -1))
    else:
        print('#{} {}'.format(tc, nums[L]))
