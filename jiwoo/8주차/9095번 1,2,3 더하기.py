T = int(input())

for i in range(T):
    dp = [0,1,2,4]   # 초기배열
    n = int(input())
    
    for j in range(4,n+1):
        dp.append(dp[j-1] + dp[j-2] + dp[j-3])  # n이 3보다 큰 경우, n번째 경우의 수 = 앞 3개의 경우의 수를 합한 것
    
    print(dp[n])