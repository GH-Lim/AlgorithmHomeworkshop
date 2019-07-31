T = int(input())

for case in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = [0] + list(map(int, input().split()))

    bus = 0    
    count = 0
    
    while bus != N:
        temp = bus
        bus += K
        
        for i in range(K):
            if bus in charge:
                count += 1
                break
            else:
                if bus == N:
                    break
                bus -= 1
                
        if bus == temp:
            count = 0
            break

    print('#{} {}'.format(case, count))
        