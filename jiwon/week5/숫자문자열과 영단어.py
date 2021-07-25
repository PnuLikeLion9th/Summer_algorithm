def solution(s):
    dict={} #치환할 값
    en=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(10):
        dict[en[i]]=i
    print(dict)

    result='' #최종 치환문자열
    eng=''
    for i in s: #문자열 하나씩 확인
        if i.isdigit(): #숫자면 그대로
            result=result+i
        elif i.isalpha(): #문자면 치환 작업
            eng=eng+i #하나씩 이어붙임
            if eng in dict.keys(): #이어붙이다가 숫자단어가 되면
                result=result+str(dict[eng]) #dict에서 찾아서 치환
                eng='' #하나씩 이어붙이는 걸 다시 새로 시작할 수 있도록 초기화
    return int(result)