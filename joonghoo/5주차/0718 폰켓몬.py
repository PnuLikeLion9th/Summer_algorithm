# 프로그래머스_폰켓몬_Set_레벨 1
# Set 자료구조를 사용해서 nums의 중복값을 제거한 set_nums의 길이와 n//2를 비교한다
# n//2 > len(set_nums)일 경우 set_nums에서 n//2개를 골라도 최댓값이 len(set_nums)에 불과하므로 len(set_nums)를 return 한다
# n//2 < len(set_nums)일 경우 폰켓몬의 종류가 n//2 보다 많다는 의미이므로 최댓값 n//2를 return 한다

def solution(nums):
    n = len(nums)
    set_nums = set(nums)  # nums의 중복된 값 제거
    if len(set_nums) < n//2:
        return len(set_nums)
    else:
        return n//2
