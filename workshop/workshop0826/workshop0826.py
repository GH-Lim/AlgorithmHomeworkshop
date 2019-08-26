import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    L = int(input())
    table = [list(map(int, input().split())) for _ in range(L)]
    first_pop = 0
    cnt = 0
    for j in range(L):
        stack = []
        for i in range(L):
            if table[i][j] != 0:
                stack.append(table[i][j])
        if len(stack):
            first_pop = stack.pop()
        while len(stack):
            next_pop = stack.pop()
            if first_pop == 2 and next_pop == 1:
                cnt += 1
            first_pop = next_pop
    print('#{} {}'.format(tc, cnt))
