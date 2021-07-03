def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr1[0])
    for i in range(row):
        for j in range(col):
            arr1[i][j]+=arr2[i][j] 
            j += 1
    return arr1