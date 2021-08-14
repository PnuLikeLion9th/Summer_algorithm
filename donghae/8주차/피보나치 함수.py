def count(n):
    if n > 2:  
        for i in range(3, n+1):
            # 피보나치 수 구하는 함수 처럼 0과 1의 호출 횟수 계산
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    return print('%d %d' %(zero[n], one[n]))


case = int(input())
for _ in range(case):
    zero = [1, 0, 1]    
    one = [0, 1, 1]
    count(int(input()))
