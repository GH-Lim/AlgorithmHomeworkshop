def del_duple(string):
    for char in string:
        if len(stack):
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)
    return len(stack)


T = int(input())
for tc in range(1, T+1):
    stack = []
    print('#{} {}'.format(tc, del_duple(input())))
