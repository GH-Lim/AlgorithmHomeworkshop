def permh():
    for i in range(len(target)):
        for candi in candis:
            for num in nums:
                if candi * 10 + num <= temp and not visit_num[candi * 10 + num]:
                    candis.append(candi * 10 + num)
                    visit_num[candi * 10 + num] = 1


def div(temp):
    global ans
    for candi in candis:
        if candi > 1:
            if temp == candi:
                dp[temp] = len(str(candi))
                return
            if temp % candi == 0 and visit_num[temp // candi]:
                if dp[temp] <= 0:
                    dp[temp] = len(str(candi)) + len(str(temp // candi)) + 1
                else:
                    dp[temp] = min(dp[temp], len(str(candi)) + len(str(temp // candi)) + 1)
            elif temp % candi == 0 and not visit_num[temp // candi]:
                if dp[temp]:
                    continue
                else:
                    div(temp // candi)
                    if not dp[temp] and dp[temp // candi] == -1:
                        dp[temp] = -1
                    else:
                        dp[temp] = len(str(candi)) + dp[temp // candi] + 1
    if not dp[temp]:
        dp[temp] = -1


for tc in range(1, int(input()) + 1):
    num_info = list(map(int, input().split()))
    # nums = [i for i in range(10) if num_info[i]]
    target = input()
    temp = int(target)
    visit_num = [0] * (temp + 1)
    nums = [i for i in range(10) if num_info[i] and i <= temp]
    for num in nums:
        visit_num[num] = 1
    candis = nums[:]
    permh()
    dp = [0] * (temp + 1)
    candis.sort(reverse=True)
    if temp > 1:
        div(temp)
        if dp[-1] == -1:
            dp[-1] -= 1
    else:
        if temp in nums:
            dp[-1] = 1
        else:
            dp[-1] = -2
    print('#%d %d' % (tc, dp[-1] + 1))
    # print(candis[:50]) # 54
    # ans = 987654321
    # if visit_num[temp]:
    #     ans = len(target)
    # else:
    #     for i in range(2, temp):
    #         for candi in candis:
    #             if candi > 1:
    #                 if candi == i:
    #                     dp[i] = len(str(i))
    #                     break
    #                 elif i % candi == 0 and visit_num[i // candi]:
    #                     if dp[i] <= 0:
    #                         dp[i] = len(str(i)) + len(str(i // candi)) + 1
    #                     else:
    #                         dp[i] = min(dp[i], len(str(i)) + len(str(i // candi)) + 1)
    #                 elif i % candi == 0 and not visit_num[i // candi]:
    #                     if dp[i]:
    #                         continue
    #                     if not dp[i] and dp[i // candi] == -1:
    #                         dp[i] = -1
    #                     else:
    #                         dp[i] = len(str(candi)) + dp[i // candi] + 1
    #         if not dp[i]:
    #             dp[i] = -1
    # print(dp)
    # print('#%d %d' % (tc, ans + 1))
