t = int(input())
 
output = []
output.insert(0, 0) 
output.insert(1, 1)                                                         # 1을 넣을 경우 경우의 수
output.insert(2, 2)                                                         # 2를 넣을 경우 경우의 수
output.insert(3, 4)                                                         # 3을 넣을 경우 경우의 수 
 
for i in range(0, t):
    n = int(input())
    for j in range(4, n+1):
        output.insert(j, output[j-1] + output[j-2] + output[j-3])
    print(output[n])
