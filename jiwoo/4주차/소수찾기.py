def solution(n):
    # 에라스토테네스의 체 방법 이용함

    n = n+1
    num = [True] * n    # n개를 모두 소수라고 가정
    count = 0
    
    for i in range(2,int(n**0.5)+1):  # n의 최대 약수가 int(n**0.5) 이하이므로 n이 아닌 int(n**0.5)로 범위 지정해줌
        if num[i] == True:            # i가 소수인 경우
            for j in range(i+i,n,i):  
                num[j] = False         # i 이후 i의 배수 = False
                
    for i in range(2,n):
        if num[i] == True:
            count += 1                # 소수 개수 세기
    return count