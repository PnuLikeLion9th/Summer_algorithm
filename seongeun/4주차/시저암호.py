#시저암호
def solution(s, n):
    upper = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ').split() #대문자를 리스트에 각각 담는다.
    lower = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()).split() #소문자를 리스트에 각각 담는다.
    s = ','.join(s).split(',')  #소문자를 리스트에 각각 담는다.
                                 
    for i in range(len(s)): #for 문을 사용해서 요소 대입 s의 길이만큼 반복
        if s[i] in upper:   #만약 s[i]가 대문자일때
            if upper.index(s[i]) + n <= 25: # 25이하일때
                s[i] = upper[upper.index(s[i])+n] #n칸 미룬 값으로 바꿔줌
            else:                   #25 이상일때 즉 a로 돌아가야 할 때
                s[i] = upper[upper.index(s[i])+n-26] #리스트의 처음으로 돌아간 다음에 다시 밀리기
        elif s[i] in lower: # 소문자일 때
            if lower.index(s[i]) + n <= 25: #아까랑 같음
                s[i] = lower[lower.index(s[i])+n]
            else:
                s[i] = lower[lower.index(s[i])+n-26]

        else:              #공백일때
            continue 

    return ''.join(s)


or

def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ': 
        	# 
            answer += ' '
            continue
        scissor = ord(i) + n
        if (ord(i) in range(ord('A'), ord('Z')+1) and scissor > ord('Z')) or \
            (ord(i) in range(ord('a'), ord('z')+1) and scissor > ord('z')):
            # c가 대문자면서 n을 더했을 때 'Z'를 넘어가는 경우
            # c가 소문자면서 n을 더했을 때 'z'를 넘어가는 경우
            answer += chr(scissor-26)
        else:
        	# 'Z'나 'z'를 넘어가지 않는 경우
            answer += chr(scissor)
        

    return answer