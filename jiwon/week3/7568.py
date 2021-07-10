for i in range(N):
    grade = 1
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            grade = grade + 1
    print(grade,end=" ")