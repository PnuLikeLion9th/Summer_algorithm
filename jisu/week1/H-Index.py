def solution(citations):
    citations.sort(reverse=True)  # 배열 내림차순 정렬
    for idx, val in enumerate(citations):
        if(idx >= val):  # 피인용수(val)가 논문수(idx)와 같거나 작을때
            return idx  # idx 리턴
    return len(citations)  # 피인용수가 같은 배열이 있을 때 (ex. [2,2])는 길이 리턴
