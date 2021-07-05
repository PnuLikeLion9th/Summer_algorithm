def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])): # 0 1 2 3
            # land[i][j] += max(land[i-1][:j+1] + land[i-1][j:])
            land[i][j] += max(land[i-1][:j] + land[i-1][j + 1:])
    return max(land[-1])
