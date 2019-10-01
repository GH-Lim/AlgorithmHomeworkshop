scores = [0] * 10001
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    visit_nums = [0]
    for num in nums:
        sub_visit = visit_nums[:]
        for vn in sub_visit:
            if not scores[vn + num]:
                visit_nums.append(vn + num)
                scores[vn + num] = 1
    print('#%d %d' % (tc, len(visit_nums)))
    if tc != T:
        for visit_num in visit_nums:
            scores[visit_num] = 0
