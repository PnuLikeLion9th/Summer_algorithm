# 프로그래머스_행렬의 덧셈_자료구조_레벨 1
# 자료구조 리스트를 이용하여 같은열, 같은행에 있는 값을 더해주면 된다.

def solution(arr1, arr2):
    answer = [[]]
    for i in range(len(arr1)):  # arr1의 1차원 list 갯수만큼 반복
        for j in range(len(arr1[i])):  # arr[i]의 길이만큼 반복
            arr1[i][j] += arr2[i][j]  # arr1와 arr2의 같은열, 같은행의 원소를 더해준다

    return arr1


arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]


print(solution(arr1, arr2))
