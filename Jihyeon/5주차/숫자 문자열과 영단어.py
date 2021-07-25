def solution(S):
    answer=''
    dic = {                                                                                 # 글자로 된 숫자를 해당 숫자로 바꾸기
        'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5',
        'six':'6', 'seven':'7', 'eight':'8', 'nine':9
    }

    answer=s
    for key, value in dic.items():                                                          # 딕셔너리에 있는 key, value 쌍을 조회해 해당 key가 존재하는 경우 해당 value로!
        answer=answer.replace(key,value)
    return int(answer)