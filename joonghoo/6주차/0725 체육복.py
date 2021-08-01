# 프로그래머스_체육복_그리디_레벨 1
# 1과 n번째의 학생은 빌려줄수 있는 사람이 1명뿐인 예외를 생각해서 풀어야한다

def solution(n, lost, reserve):
    student = [0] + [1] * n
    for i in reserve:  # 여분의 체육복을 가져온 학생들
        student[i] = 2
    for i in lost:  # 체육복을 잃어버린 학생들
        student[i] -= 1

    for i in range(1, n+1):
        if i == 1:  # 첫번째에 해당하는 학생은 두 번째의 해당하는 학생에게만 체육복을 나눠줄수있다
            if student[1] == 2 and student[2] == 0:
                student[1] = 1
                student[2] = 1
        elif i == n:  # 마지막 학생은 n-1번째 해당하는 학생에게만 체육복을 나누어줄수 있다
            if student[n] == 2 and student[n-1] == 0:
                student[n] = 1
                student[n-1] = 1
        else:  # 나머지 학생들은 앞뒤 확인하여 체육복을 나누어주면 된다
            if student[i] == 2:
                if student[i-1] == 0:
                    student[i] = 1
                    student[i-1] = 1
                elif student[i+1] == 0:
                    student[i] = 1
                    student[i+1] = 1

    return student.count(1) + student.count(2)


print(solution(5, [2, 4], [3]))
