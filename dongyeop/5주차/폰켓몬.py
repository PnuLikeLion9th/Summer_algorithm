def solution(nums):
    n = len(nums)#주어진 리스트의 길이
    stack = list()#뽑은 폰켓몬을 넣어줄 스택
    for i in range(n):
        if len(stack)==n/2:#절반만큼 뽑으면 중단
            break
        if nums[i] not in stack:#스택에 없으면 추가
            stack.append(nums[i])
        else:
            continue
    return len(stack)