import sys
sys.stdin = open('input.txt', 'r')


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


def check_code(decoded):
    if (sum(decoded[0::2]) * 3 + sum(decoded[1::2])) % 10:
        return 0
    else:
        return sum(decoded)


def find_n(bcode, idx):
    i = idx
    cnt = 0
    while True:
        if bcode[i - 1] != bcode[i] or i - 1 < 0:
            cnt += 1
        if cnt == 4:
            break
        i -= 1
    len_num = idx - i + 1
    return len_num // 7


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    checked = []
    sum_codes = 0
    temp = 'a'
    for _ in range(N):
        codes = int(input(), 16)
        if codes == 0:
            continue
        bin_code = bin(codes)[2:].rstrip('0').zfill(M * 4)
        if bin_code == temp:
            continue
        else:
            temp = bin_code

        len_b = len(bin_code)
        i = len_b - 1
        while i >= 0 and int(bin_code[:i]):
            if bin_code[i] == '0':
                i -= 1
            elif bin_code[i] == '1':
                n = find_n(bin_code, i)
                code = bin_code[i - 56 * n + 1: i + 1]
                if code not in checked:
                    checked.append(code)
                    sum_codes += check_code(decode(code, n))
                i -= 56 * n

    print('#{} {}'.format(tc, sum_codes))
