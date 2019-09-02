T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    password = list(map(int, input().split()))
    idx = 0
    L = N
    for i in range(K):
        idx += M
        if idx == L:
            password.insert(idx, password[idx-1]+password[0])
        else:
            idx %= L
            password.insert(idx, password[idx-1] + password[idx])
        L += 1
    pwlen = len(password) if len(password) <= 10 else 10

    print('#{}'.format(tc), end='')
    for i in range(pwlen):
        print('', password[-1-i], end='')
    print()
