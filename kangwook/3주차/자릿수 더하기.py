def solution(N):
    answer=0
    for i in str(N):
        i=int(i)
        answer+=i
    return answer
#자릿수를 구하기 위해 문자열로 바꿔주었고, 각 문자열을 다시 정수로 바꿔서 합을 answer에 담았다.
