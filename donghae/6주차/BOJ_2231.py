n= int(input())
res = 0
for i in range(0,n+1):  #n까지의 수 모두 계산
    n_sum = list(map(int, str(i)))  #자릿수 합 구하기
    res = i+sum(n_sum)  #분해합 구해서 res에 넣기
    if n == res:   
        print(i)    #생성자 찾으면 출력 후 break
        break;
    if n == i:
        print(0)
