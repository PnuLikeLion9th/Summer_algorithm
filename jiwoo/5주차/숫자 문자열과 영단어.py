def solution(s):
    dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

    for key in dic:         # dic의 key값만 들고오기     
            s = s.replace(key, str(dic[key]))  # s에 존재하는 key값들을 val값으로 바꾸기
    
    return int(s)