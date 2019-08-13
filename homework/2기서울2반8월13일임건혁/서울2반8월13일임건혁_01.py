T = int(input())

for tc in range(1, T + 1):
    string = input()
    target = input()
    i = 0
    result = 0
    for i in range(len(target) - len(string) + 1):
        c = 0
        while c < len(string):
            if string[c] != target[i + c]:
                break
            else:
                c += 1
        if c == len(string):
            result = 1
            break
    print('#%d %d' % (tc, result))
