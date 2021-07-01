n = int(input())
cycle = 0
num = n

while True:
    a = num//10      # num의 10의 자리 수
    b= num%10        # num의 1의 자리 수
    c = (a+b)%10     # num의 자릿수 더한 것의 1의 자리 수
    num = b*10 + c   # b와 c 합해 새로운 수 생성
    cycle = cycle + 1  
    
    if num == n:    # 새로운 수와 기존의 수 같다면 while문 빠져나오기
        break

print(cycle) 