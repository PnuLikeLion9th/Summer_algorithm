count_0 = [1,0,1]   # 0이 출력되는 개수 초기배열
count_1 = [0,1,1]   # 1이 출력되는 개수 초기배열

def fibo(n):
    if len(count_0) <= n:
        for i in range(len(count_0),n+1):
            count_0.append(count_0[i-1] + count_0[i-2])   # 피보나치 수열로 값 구해서 배열에 추가
            count_1.append(count_1[i-1] + count_1[i-2])
    print(count_0[n], count_1[n])

n = int(input())

for i in range(n):
    fibo(int(input()))