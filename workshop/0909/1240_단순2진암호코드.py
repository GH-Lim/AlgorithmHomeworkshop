import sys
sys.stdin = open('input.txt', 'r')
def find_last():
    for i in range(5, N - 4):
        for j in range(M - 1, 56, -1):
            if code[i][j] == '1':
                return i, j - 55
    return -1, -1


decoder = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    code = list(input() for _ in range(N))
    i, j = find_last()
    if i == -1:
        print('#{} 0'.format(tc))
    else:
        decode = []
        for k in range(8):
            num = code[i][j + k * 7: j + k * 7 + 7]
            decode.append(decoder[num])
        if (sum(decode[0::2]) * 3 + sum(decode[1::2])) % 10:
            print('#{} 0'.format(tc))
        else:
            print('#{} {}'.format(tc, sum(decode)))
