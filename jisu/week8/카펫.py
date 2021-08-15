def solution(brown, yellow):
    total = brown+yellow
    for i in range(total//2, 0, -1):
        if total % i:
            continue
        width, height = i, total/i
        if (width-2)*(height-2) == yellow:
            return [width, height]
