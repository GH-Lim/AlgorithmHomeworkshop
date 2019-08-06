import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    bolts = input().split()
    m_bolts = [bolts[i * 2] for i in range(n)]
    f_bolts = [bolts[i*2 + 1] for i in range(n)]
    result = [0] * (2*n)

    for i in range(n):
        isFirst = True
        for j in range(n):
            if m_bolts[i] == f_bolts[j]:
                isFirst = False
        if isFirst:
            next_index = i
            break

    for i in range(n):
        result[i * 2] = m_bolts[next_index]
        result[i*2 + 1] = f_bolts[next_index]
        for j in range(n):
            if f_bolts[next_index] == m_bolts[j]:
                next_index = j
                break
    print('#{} {}'.format(tc, ' '.join(result)))
