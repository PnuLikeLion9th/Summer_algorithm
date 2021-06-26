def solution(arr1, arr2):
    answer = [[]]
    #for문 앞쪽에 list 형식을 쓰면 for문을 수행하며 list로 요소를 반환함.
    #1. [1,2] [3,4] / [2,3] [5,6]
    #2. [1,3] [2,4] / [2,5] [3,6]
    #3. [4, 6] / [7, 9]

    #zip은 [1,2][3,4]의 리스트를 ([1,3][2,4])로 변환해준다. 반환값은 튜플임
    answer = list([x+y for x, y in list(zip(a, b))] for a, b in list(zip(arr1, arr2)))
    return answer

print(solution([[1,2],[2,3]],	[[3,4],[5,6]]	))