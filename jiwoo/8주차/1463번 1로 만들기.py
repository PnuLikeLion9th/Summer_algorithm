n = int(input())
a = [0]*(n+1) 

for i in range(2,n+1):  # 1은 0이기 때문에 2부터 시작
    a[i] = a[i-1] + 1

    if i%2 == 0:      # 2로 나누어질 경우, a[i-1] + 1과 비교해 최솟값 저장
        a[i] = min(a[i], a[i//2]+1)
    
    if i%3 == 0:      # 3으로 나누어질 경우, a[i-1] + 1과 비교해 최솟값 저장
        a[i] = min(a[i], a[i//3]+1)

print(a[n])