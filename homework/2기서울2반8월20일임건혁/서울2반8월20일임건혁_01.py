def paper_paste(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return paper_paste(N - 10) + 2 * paper_paste(N - 20)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(tc, paper_paste(N)))
