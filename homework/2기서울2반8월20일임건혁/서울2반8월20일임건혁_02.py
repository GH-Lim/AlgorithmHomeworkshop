def is_correct(code):
    stack = []
    for char in code:
        if char == '{' or char == '(':
            stack.append(char)
        elif char == '}':
            if not len(stack):
                return 0
            if stack.pop() != '{':
                return 0
        elif char == ')':
            if not len(stack):
                return 0
            if stack.pop() != '(':
                return 0
        else:
            continue
    if len(stack):
        return 0
    return 1


def is_correct_2(code):
    stack = [0] * len(code)
    top = -1
    for i in range(len(code)):
        if code[i] == '{' or code[i] == '(':
            top += 1
            stack[top] = code[i]
        elif code[i] == '}':
            if top == -1:
                return 0
            if stack[top] != '{':
                return 0
            else:
                stack[top] = 0
                top -= 1
        elif code[i] == ')':
            if top == -1:
                return 0
            if stack[top] != '(':
                return 0
            else:
                stack[top] = 0
                top -= 1
        else:
            continue
    if top > -1:
        return 0
    return 1


T = int(input())
for tc in range(1, T + 1):
    # print('#{} {}'.format(tc, is_correct(input())))
    print('#{} {}'.format(tc, is_correct_2(input())))
