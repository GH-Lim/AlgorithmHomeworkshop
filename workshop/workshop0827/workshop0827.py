import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    L = int(input())
    string = input()
    result = []
    operator = []
    for token in string:
        if token == '(':
            operator.append('(')
        elif token == ')':
            while operator[-1] != '(':
                result.append(operator.pop())
            operator.pop()
        elif token == '+':
            while operator[-1] != '(':
                result.append(operator.pop())
            if operator[-1] == '(':
                operator.append('+')
        elif token == '*':
            if operator[-1] == '(' or operator[-1] == '+':
                operator.append('*')
            else:
                result.append('*')
        else:
            result.append(int(token))
    stack = []
    for token in result:
        if token == '+':
            sum_token = stack.pop() + stack.pop()
            stack.append(sum_token)
        elif token == '*':
            mul_token = stack.pop() * stack.pop()
            stack.append(mul_token)
        else:
            stack.append(token)
    print('#{} {}'.format(tc, stack[0]))
