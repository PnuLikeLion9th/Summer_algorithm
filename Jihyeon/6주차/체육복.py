# 그리디 : 최적해를 구하는 데에 사용되는 근사적인 방법/ 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달하는 알고리즘
# set : 집합 자료형 / 중복을 허용하지 않고 순서가 없음

def solution(n, lost, reserve):
    reserve_n = list(set(reserve)-set(lost))    # 체육복을 잃어버린 사람 중 여벌옷이 있는 사람은 제외(set 이용)
    lost_n = list(set(lost)-set(reserve)

    answer = n-len(lost_n)                     # 이미 체육복을 가진 학생 수
    for i in lost_n:
        if i - 1 in reserve_n:                  # reserve_n에 앞순서, 뒷순서에 체육복 가진 학생이 있는 경우
            answer += 1                         # reserve_n에서 삭제하고 answer에 1을 늘림
            reserve_n.remove(i-1)
        elif i +1 in reserve_n:
            answer += 1
            reserve_n.remove(i+1)

    return answer