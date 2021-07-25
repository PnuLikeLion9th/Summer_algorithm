num = int(input())
line = 0
line_max = 0
while num > line_max:   #몇 번째 라인인지 구하기
    line += 1
    line_max += line
if line%2 == 0: #지그재그로 움직이기 때문에 라인 짝/홀 구분 
    a = line - (line_max-num)
    b = (line_max-num) + 1
else:
    a = (line_max-num) + 1
    b = line - (line_max-num)
print(f'{a}/{b}')   #f 문자열 포매팅으로 출력
