T = int(input())
for tc in range(1, T + 1):
    b_num = list(map(int, input()))
    t_num = list(map(int, input()))
    len_b = len(b_num)
    len_t = len(t_num)
    b_candidate = []
    for i in range(len_b):
        if b_num[i] == 0:
            b_num[i] = 1
            candidate = 0
            for j in range(len_b):
                candidate += b_num[len_b - 1 - j] * (2 ** j)
            b_candidate.append(candidate)
            b_num[i] = 0
        else:
            b_num[i] = 0
            candidate = 0
            for j in range(len_b):
                candidate += b_num[len_b - 1 - j] * (2 ** j)
            b_candidate.append(candidate)
            b_num[i] = 1

    for i in range(len_t):
        if t_num[i] == 0:
            t_num[i] = 1
            candidate = 0
            for j in range(len_t):
                candidate += t_num[len_t - 1 - j] * (3 ** j)
            if candidate in b_candidate:
                result = candidate
                break
            t_num[i] = 2
            candidate = 0
            for j in range(len_t):
                candidate += t_num[len_t - 1 - j] * (3 ** j)
            if candidate in b_candidate:
                result = candidate
                break
            t_num[i] = 0
        elif t_num[i] == 1:
            t_num[i] = 0
            candidate = 0
            for j in range(len_t):
                candidate += t_num[len_t - 1 - j] * (3 ** j)
            if candidate in b_candidate:
                result = candidate
                break
            t_num[i] = 2
            candidate = 0
            for j in range(len_t):
                candidate += t_num[len_t - 1 - j] * (3 ** j)
            if candidate in b_candidate:
                result = candidate
                break
            t_num[i] = 1
        else:
            t_num[i] = 0
            candidate = 0
            for j in range(len_t):
                candidate += t_num[len_t - 1 - j] * (3 ** j)
            if candidate in b_candidate:
                result = candidate
                break
            t_num[i] = 1
            candidate = 0
            for j in range(len_t):
                candidate += t_num[len_t - 1 - j] * (3 ** j)
            if candidate in b_candidate:
                result = candidate
                break
            t_num[i] = 2
    print('#{} {}'.format(tc, result))
