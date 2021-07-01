def solution(n):
    count =0 #몇번 반복하는지 세는 count 할당
    while n>1:
        if n%2==0:#짝수일떄
            n= n/2
            count +=1
        elif n%2!=0:#홀수일때
            n=n*3+1
            count +=1
        if count>=500:#500회 이상 넘어가면 반복문을 중단할 if문
            return -1
    return count #count를 반환