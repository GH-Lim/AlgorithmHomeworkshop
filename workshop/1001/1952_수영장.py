def check(m, price):
    global ans
    if m >= 12:
        ans = price
        return
    if not plans[m]:
        check(m + 1, price)
    else:
        if plans[m] * day < m_1:
            if price + plans[m] * day < ans:
                check(m + 1, price + plans[m] * day)
        else:
            if price + m_1 < ans:
                check(m + 1, price + m_1)
        if price + m_3 < ans:
            check(m + 3, price + m_3)


for tc in range(1, int(input()) + 1):
    day, m_1, m_3, year = map(int, input().split())
    plans = list(map(int, input().split()))
    ans = year
    check(0, 0)
    print('#%d %d' % (tc, ans))
