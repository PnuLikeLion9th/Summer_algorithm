def solution(s,n):
    word=s.split(' ')   #띄어쓰를 기준으로 글자를 나눈다.
    answer_=[]  #빈 리스트를 하나 만들고
    for j in range(int(len(word))): 
        x=str(word[j])  #글자를 나눈 리스트에서 하나씩 뽑는다
        y=[]    #빈 리스트를 하나 더 만들고 
        for i in range(int(len(x))):    
            k=ord(x[i])     #단어의 글자를 하나씩 아스키코드 +n씩 해준다
            if k==90:
                k=65+n-1
            elif k== 122:
                k=97+n-1
            else:
                k+=n
            z=chr(k)
            y.append(str(z))    #처리한 글자를 y 리스트에 담는다.
        answer_.append(str("".join(y)))
    answer= " ".join(answer_)
    return answer