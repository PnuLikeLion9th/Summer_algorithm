n = int(input())    #테스트 케이스 수
for i in range(n):
    num, s = input().split()
    for j in s:
        print(j*int(num), end='')   #num만큼 문자 반복
    print() #줄바꿈