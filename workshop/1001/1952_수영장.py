# def check(m, price):
#     global ans
#     if m >= 12:
#         ans = price
#         return
#     if not plans[m]:
#         check(m + 1, price)
#     else:
#         if plans[m] * day < m_1:
#             if price + plans[m] * day < ans:
#                 check(m + 1, price + plans[m] * day)
#         else:
#             if price + m_1 < ans:
#                 check(m + 1, price + m_1)
#         if price + m_3 < ans:
#             check(m + 3, price + m_3)
#
#
# for tc in range(1, int(input()) + 1):
#     day, m_1, m_3, year = map(int, input().split())
#     plans = list(map(int, input().split()))
#     ans = year
#     check(0, 0)
#     print('#%d %d' % (tc, ans))

dp = [0] * 12  # 0 ~ 11 ==> 1월부터 12월까지의 최소값 저장
cost = [10, 40, 100, 300]  # 1일, 1달, 3달, 12달
plan = [0, 0, 2, 9, 1, 5, 0, 0, 0, 0, 0, 0]
dp[0] = min(plan[0] * cost[0], cost[1])  # 1월의 최소 cost를 초기값으로 지정하기
for i in range(1, 12):
    dp[i] = dp[i - 1] + min(plan[i] * cost[0], cost[1])
    # 직전 월의 하루요금 * 계획일수 and 한달 요금 비교하기
    if i >= 3: # 3 이상부터 3달치 요금과도 비교하기
        dp[i] = min(dp[i - 3] + cost[2], dp[i])
        # 3달 요금이 더 작다면 최신화하기
result = min(dp[-1], cost[3])
# 위에서 계산한 12월 까지의 최소 요금 vs 1년 요금 비교하기
print(dp)
print(result)
'''
[0, 0, 20, 60, 70, 110, 110, 110, 110, 110, 110, 110]
110
'''