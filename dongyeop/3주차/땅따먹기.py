def solution(land):
    #바로 아래에 같은열을 선택할수 없다.최대의 값을 뽑아내야 함으로 같은열값을 제외한 나머지들중에서 가장 큰값을 더한다.
    for i in range(len(land)-1):
        land[1+i][0] += max(land[i][1],land[i][2],land[i][3])
        land[1+i][1] += max(land[i][0],land[i][2],land[i][3])
        land[1+i][2] += max(land[i][0],land[i][1],land[i][3])
        land[1+i][3] += max(land[i][0],land[i][1],land[i][2])
    return max(land[len(land)-1])
