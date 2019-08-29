import sys
from collections import deque
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    q = deque(input())
    cards = {}
    marks = ['S', 'D', 'H', 'C']
    for mark in marks:
        cards[mark] = deque()
    overlapped = False
    while q and not overlapped:
        temp = q.popleft()
        number = int(q.popleft())*10 + int(q.popleft())
        if number not in cards[temp]:
            cards[temp].append(number)
            continue
        else:
            overlapped = True
            break
    if overlapped:
        print('#{} ERROR'.format(tc))
    else:
        result = [str(13-len(cards[mark])) for mark in marks]
        print('#{} {}'.format(tc, ' '.join(result)))
