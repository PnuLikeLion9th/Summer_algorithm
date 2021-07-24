def solution(s):
    num = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7','eight':'8', 'nine':'9'}
    res = ''
    word = ''
    for i in s:
        if i in num.values():   #i가 key값 중에 있는 경우
            res += i
        else:   
            word += i
            if word in num.keys():  #만약 word가 value값 중에 있는 경우 
                res += num.get(word)
                word = ''   #다음 문자를 찾기 위해 초기화
    return int(res)
    #딕셔너리와 replace 함수 사용하면 더 간단하게 풀 수 있음