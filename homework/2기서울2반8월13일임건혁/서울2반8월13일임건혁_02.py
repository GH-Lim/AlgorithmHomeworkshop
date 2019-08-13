def palin(arr, N, M):
    for i in range(N):
        for j in range(N - M + 1):
            m = 0
            is_palin_col = True
            is_palin_row = True
            while 1:
                if is_palin_row:
                    if arr[i][j + m] != arr[i][j + M - 1 - m]:
                        is_palin_row = False
                if is_palin_col:
                    if arr[j + m][i] != arr[j + M - 1 - m][i]:
                        is_palin_col = False
                if is_palin_col or is_palin_row:
                    m += 1
                else:
                    break
                if m == M // 2:
                    palin_word = ''
                    for k in range(M):
                        if is_palin_row:
                            palin_word += arr[i][j+k]
                        else:
                            palin_word += arr[j+k][i]
                    return palin_word


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [0] * N
    for i in range(N):
        arr[i] = input()
    print('#{} {}'.format(tc, palin(arr, N, M)))
