def solution(nums):
    num = len(nums)/2   # 선택할 수 있는 폰켓몬 수
    nums = set(nums)    # 중복되는 폰켓몬 종류 제거
    
    if len(nums) > num:   # 중복을 제외한 폰켓몬 종류가 선택할 수 있는 폰켓몬 수보다 많을 경우
        return num
    else:
        return len(nums)