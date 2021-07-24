#동적 프로그래밍 (피보나치수열 바텀업 방식)
n = int(input())
for i in range(n):
    zero = [1,0,1]#t가 0,1,2일떄 0이 나오는 횟수
    one = [0,1,1]#t가 0,1,2일때 1이 나오는 횟수
    t = int(input())
    if t>=3:
        for j in range(3,t+1):
            zero.append(zero[j-1]+zero[j-2])
            one.append(one[j-1]+one[j-2])
    print(zero[t],one[t])
