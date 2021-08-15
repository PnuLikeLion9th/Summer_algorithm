n = int(input())
stair = []
dp=[]
for i in range(n):
    stair.append(int(input()))
dp.append(stair[0])
dp.append(max(stair[0]+stair[1],stair[1]))
dp.append(max(stair[0]+stair[2],stair[1]+stair[2]))

for i in range(3,n):
    dp.append(max(dp[i-2]+stair[i],dp[i-3]+stair[i]+stair[i-1]))

print(dp[-1])