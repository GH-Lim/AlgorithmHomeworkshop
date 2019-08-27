import sys
sys.stdin = open('input.txt', 'r')
#
# for tc in range(1, 11):
#     L = int(input())
#     string = input()
#     result = []
#     operator = []
#     for token in string:
#         if token == '(':
#             operator.append('(')
#         elif token == ')':
#             while operator[-1] != '(':
#                 result.append(operator.pop())
#             operator.pop()
#         elif token == '+':
#             while operator[-1] != '(':
#                 result.append(operator.pop())
#             if operator[-1] == '(':
#                 operator.append('+')
#         elif token == '*':
#             if operator[-1] == '(' or operator[-1] == '+':
#                 operator.append('*')
#             else:
#                 result.append('*')
#         else:
#             result.append(int(token))
#     stack = []
#     for token in result:
#         if token == '+':
#             sum_token = stack.pop() + stack.pop()
#             stack.append(sum_token)
#         elif token == '*':
#             mul_token = stack.pop() * stack.pop()
#             stack.append(mul_token)
#         else:
#             stack.append(token)
#     print('#{} {}'.format(tc, stack[0]))

for t in range(1, 11):
    N = int(input())
    cal_list = input()

stack = []
result = ''

icp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, ')': 0}

for c in cal_list:
    print(c)
    # ( : stack에 그대로 쌓기
    if c == '(':
        stack.append(c)
        print(stack, result)
    # +, - : [-1]이 (면 그대로 쌓고, *나 /가 있으면 pop해서 출력
    elif c == '+':
        if len(stack) == 0:
            stack.append('+')
            print(stack, result)
        elif icp[stack[-1]] == 0:
            stack.append('+')
            print(stack, result)
        else:
            while icp[stack[-1]] >= 1:
                result += stack[-1]
                stack.pop()
                print(stack, result)
    elif c == '-':
        if len(stack) == 0:
            stack.append('-')
            print(stack, result)
        elif icp[stack[-1]] == 0:
            stack.append('-')
            print(stack, result)
        else:
            while icp[stack[-1]] >= 1:
                result += stack[-1]
                stack.pop()
                print(stack, result)

    elif c == '*':
        if len(stack) == 0:
            stack.append('*')
            print(stack, result)
        elif icp[stack[-1]] < 2:
            stack.append('*')
            print(stack, result)

        else:
            while icp[stack[-1]] >= 2:
                result += stack[-1]
                stack.pop()
                print(stack, result)

    elif c == '/':
        if len(stack) == 0:
            stack.append('/')
            print(stack, result)
        elif icp[stack[-1]] < 2:
            stack.append('/')
            print(stack, result)
        else:
            while icp[stack[-1]] >= 2:
                result += stack[-1]
                stack.pop()
                print(stack, result)
        # ) : ( 나올때까지 계속 pop하면서 기호를 result에 더해주기

    elif c == ')':
        print('stack = {}'.format(stack[-1]))
        while stack[-1] != '(':
            result += stack[-1]
            stack.pop()
            print(stack, result)
        stack.pop()
        # 기호가 아닌 숫자가 나오면
    else:
        result += c
    print(stack, result)

    print(result)
