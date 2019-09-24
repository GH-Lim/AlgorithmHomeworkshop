def comb(i, total):
    global ans
    ans = min(total, ans)
    if i == N - 1:
        return
    if total - L[i + 1] >= B:
        comb(i + 1, total - L[i + 1])
    comb(i + 1, total)


for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    L = list(map(int, input().split()))
    ans = sum(L)
    comb(-1, ans)
    print('#%d %d' % (tc, ans - B))
