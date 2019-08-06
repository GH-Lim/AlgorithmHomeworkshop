T = int(input())

for tc in range(1, T + 1):
    field = [[0 for r in range(10)] for c in range(10)]
    N = int(input())
    purple = 0
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if field[i][j] != color:
                    field[i][j] += color
                    if field[i][j] == 3:
                        purple += 1
    print('#{} {}'.format(tc, purple))
