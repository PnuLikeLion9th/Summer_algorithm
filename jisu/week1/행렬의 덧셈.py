def solution(arr1, arr2):
    for i in range(len(arr1)): #arr1의 길이만큼 반복 (첫번째 예시 기준: 두번(0,1))
        for j in range(len(arr1[0])): #arr1[0]의 길이만큼 반복 (첫번째 예시 기준: 네번(0,1,0,1))
            arr1[i][j] += arr2[i][j] #arr1[i][j]에 arr2[i][j]를 더해준다. (즉 같은 행, 열의 요소들끼리 합해줌)
    return arr1