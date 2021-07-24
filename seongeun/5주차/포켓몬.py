#포켓몬
'''전략: 새로 만든 리스트와 비교해서 값이 없으면 추가하고 있으면 넘어가기. 
         길이가 nums의 반이 되면 for문 중지하고 리스트의 길이 return '''

def solution(nums):
    a = []        #새로 추가할 리스트 만들어놓기

    for i in range(len(nums)) :  #0부터 num길이만큼 반복
        if len(a) == len(nums)/2 : #a길이가 nums길이의 반이 되면
            break                  # 중지
        elif nums[i] in a :        # nums[i]가 리스트 안에 있으면
            pass                   # 걍 넘어가기
        else :                     # 리스트 안에 없으면
            a.append(nums[i])      # 리스트에 추가하기
    return len(a)                  # 리스트 길이 출력
