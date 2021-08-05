def find_clock_num(num):
    clock_num = num
    for _ in range(3):
        num = (num % 1000 ) * 10 + num // 1000
        if clock_num > num :
            clock_num = num
        return clock_num
    
clock_num = find_clock_num(int(''.join(input().split())))

i = 111
cnt = 0
while(i<=clock_num):
    if find_clock_num(i) == i:
        cnt += 1
    i += 1
print(cnt)