def solution(nums):
    answer=0                    
    pick=len(nums)/2            #  nums의 길이 반이 고를 수 있는 폰켓몬의 수
    nums=list(set(nums))        # nums를 집합 자료형으로 변환해서 중복 제거 -> 다시 리스트 변환

    if len(nums)>=pick:         # 중복 제거한 nums 길이가 pick과 크거나 같은 경우
        answer=pick
    elif len(nums)<pick:        # nums의 길이가 pick보다 작은 경우
        answer=len(nums)

    return answer