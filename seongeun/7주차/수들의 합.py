# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

n = int(input())
i = 1
while i * (i+1) // 2 <= n: #1부터 i까지의 합이 n이 될 때ㅏ까지
    i += 1  #i에 1 더해줌
print(i-1) #i-1 print