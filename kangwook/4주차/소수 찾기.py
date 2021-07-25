def solution (n):
    count=0
    for i in range(2,n+1):
    # 입력된 범위내에서 자연수 1씩 증가하면서 소수인지 체크하려고 for문으로 꺼낸다.
        for j in range(2,int(i/2)+1):
        # 체크하려는 자연수 i가 소수인지 판단하는 코드. for문을 사용한다. 
        # j는 약수의 가능성을 가진 숫자. 1씩 증가
            if i%j == 0:
                break
        else :
            count+=1
    return count