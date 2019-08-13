T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    sub_str1 = str1[0]
    for i in range(1, len(str1)):
        j = 0
        while j < len(sub_str1):
            if str1[i] == sub_str1[j]:
                break
            else:
                j += 1
        if j == len(sub_str1):
            sub_str1 += str1[i]
    max_num = 0
    for i in range(len(sub_str1)):
        count = 0
        for j in range(len(str2)):
            if sub_str1[i] == str2[j]:
                count += 1
        max_num = count if count > max_num else max_num
    print('#%d %d' % (tc, max_num))