def solution(a,b):
    for i in range(len(a)):#arr1의 길이만큼 반복
        for j in range(len(a[i])):#arr1[i]만큼 반복
            a[i][j] = a[i][j]+b[i][j]#a[i][j]에 두 배열 [i][j]요소 합 할당
    return a
        