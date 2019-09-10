import sys
sys.stdin = open('input.txt', 'r')


def right_bottom(a, b):
    while codes[a + 1][b] != '0':
        a += 1
    while codes[a][b + 1] != '0':
        b += 1
    return a, b


def decode(code, n):
    result = []
    decoder = {
        '0' * 3 * n + '1' * 2 * n + '0' * 1 * n + '1' * 1 * n: 0,
        '0' * 2 * n + '1' * 2 * n + '0' * 2 * n + '1' * 1 * n: 1,
        '0' * 2 * n + '1' * 1 * n + '0' * 2 * n + '1' * 2 * n: 2,
        '0' * 1 * n + '1' * 4 * n + '0' * 1 * n + '1' * 1 * n: 3,
        '0' * 1 * n + '1' * 1 * n + '0' * 3 * n + '1' * 2 * n: 4,
        '0' * 1 * n + '1' * 2 * n + '0' * 3 * n + '1' * 1 * n: 5,
        '0' * 1 * n + '1' * 1 * n + '0' * 1 * n + '1' * 4 * n: 6,
        '0' * 1 * n + '1' * 3 * n + '0' * 1 * n + '1' * 2 * n: 7,
        '0' * 1 * n + '1' * 2 * n + '0' * 1 * n + '1' * 3 * n: 8,
        '0' * 3 * n + '1' * 1 * n + '0' * 1 * n + '1' * 2 * n: 9,
    }
    for i in range(8):
        result.append(decoder[code[i * n * 7: (i+1) * n * 7]])
    return result


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    codes = list(input() for _ in range(N))
    visited = [[0] * M for _ in range(N)]
    sum_results = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and codes[i][j] != '0':
                a, b = right_bottom(i, j)
                for k in range(i, a + 1):
                    for l in range(j, b + 1):
                        visited[k][l] = 1
                code = bin(int(codes[i][j:b + 1], 16))[2:]
                n = (len(code) + 3) // 56
                code = code.rstrip('0').zfill(56 * n)
                result = decode(code, n)
                if (sum(result[0::2]) * 3 + sum(result[1::2])) % 10:
                    continue
                else:
                    sum_results += sum(result)
    print('#{} {}'.format(tc, sum_results))
