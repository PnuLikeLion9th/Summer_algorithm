#전체학생수 n 체육벌 도난당한 학생등의 배열 lost 여벌 체육복 가진 학생들의 배열 reverse
def solution(n,lost,reserve):
    answer=n-len(lost)#여분이 있는 학생이 잃어버렸을경우에는 빌려줄수없기때문에 먼저 제거해주도록하자.(테스트케이스 5 7 12 에러걸림)
    for i in lost[:]:#바로 lost에서 remove를 하면 i가 하나 건너뜀 고래서 복제로 for문 돌림
        if i in reserve:
            answer+=1
            reserve.remove(i)
            lost.remove(i)
    for i in lost:
        if i+1 in reserve:
            answer+=1
            reserve.remove(i+1)
        elif i-1 in reserve:
            answer+=1
            reserve.remove(i-1)
    return answer

