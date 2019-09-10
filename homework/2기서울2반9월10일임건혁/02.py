T = int(input())
for tc in range(1, T + 1):
    num = float(input())
    result = []
    i = 0
    while num != 0 and i <= 12:
        num *= 2
        a = int(num // 1)
        num %= 1
        result.append(a)
        i += 1
    print('#%d' % tc)
    if num:
        for bit in result:
            print(bit, end='')
            print()
    else:
        print('overflow')
