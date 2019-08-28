# import sys
# sys.stdin = open('01.txt', 'r')


def forth(S):
    stack = [0] * len(S)
    operators = ['+', '-', '/', '*']
    top = -1
    for token in S:
        if token in operators:
            if top < 1:
                return 'error'
            if token == '+':
                result = stack[top] + stack[top - 1]
                top -= 1
                stack[top] = result
            elif token == '*':
                result = stack[top] * stack[top - 1]
                top -= 1
                stack[top] = result
            elif token == '/':
                result = stack[top - 1] // stack[top]
                top -= 1
                stack[top] = result
            elif token == '-':
                result = stack[top - 1] - stack[top]
                top -= 1
                stack[top] = result
        elif token == '.':
            if top == 0:
                return stack[top]
            else:
                return 'error'
        elif token.isdigit():
            top += 1
            stack[top] = int(token)
        else:
            return 'error'


T = int(input())
for tc in range(1, T + 1):
    L = input().split()
    print('#{} {}'.format(tc, forth(L)))
