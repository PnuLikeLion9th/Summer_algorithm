def solution(nums):
    nums_set=set(nums)  #종류를 알기 위해 set으로 변환 (중복 제거)
    if len(nums)/2 >= len(nums_set):    #if문을 통한 값 도출
        answer = len(nums_set)
    else:
        answer = len(nums)/2
    return answer