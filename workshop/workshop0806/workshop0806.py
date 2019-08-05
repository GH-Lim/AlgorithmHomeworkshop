import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    bolts = input().split()
    m_bolts = bolts[0::2]
    f_bolts = bolts[1::2]
    result = [0] * 2 * n

    for i in range(n):
        if m_bolts[i] not in f_bolts:
            next_index = i
    for i in range(n):
        result[2 * i] = m_bolts[next_index]
        result[2 * i + 1] = f_bolts[next_index]
        for j in range(n):
            if f_bolts[next_index] == m_bolts[j]:
                next_index = j
                break
    print('#{} {}'.format(tc, ' '.join(result)))
