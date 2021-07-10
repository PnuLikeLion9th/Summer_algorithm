a = list(input().upper())    # 입력된 단어 모두 대문자로 변경
b = [0]*26

for i in a:
    b[ord(i)-65] += 1        # 알파벳이 사용될 때마다 해당 리스트 위치에 1 추가

max_index = b.index(max(b))  #  리스트 b에서 가장 큰 수의 인덱스를 max_index 값에 저장 

if b.count(max(b)) > 1:      # 만약 가장 큰 수가 여러 개 존재할 경우,
    print('?')               # ? 출력
else:
    print(chr(max_index+65)) # 아니면, max_index 값을 chr() 이용해 알파벳으로 출력