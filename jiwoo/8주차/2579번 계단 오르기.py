n = int(input())
a = [0]*301        # 계단의 점수
sum = [0]*301      # 해당 칸까지 얻을 수 있는 최대 점수

for i in range(n):
    a[i] = int(input())

sum[0] = a[0]
sum[1] = a[0]+a[1]
sum[2] = max(a[0]+a[2],a[1]+a[2])  # 1칸점프 후 2칸점프, 2칸점프 후 1칸점프 중 최댓값

for i in range(3,n):
    sum[i] = max(a[i]+a[i-1]+sum[i-3],a[i]+sum[i-2]) # 그 전 계단을 밟은 경우와 아닌 경우 중 최댓값

print(sum[n-1])