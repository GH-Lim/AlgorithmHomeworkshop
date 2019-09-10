T = int(input())
for tc in range(1, T + 1):
    print('#%d' % tc, end=' ')
    L, hex_num = input().split()
    for num in hex_num:
        print(bin(int(num, 16))[2:].zfill(4), end='')
    print()