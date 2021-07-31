def solution(answers):
    a = [1,2,3,4,5] #반복 제외한 a,b,c 정의
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    cnt = [0,0,0]   #a,b,c 점수 카운트 리스트 정의
    for i in range(len(answers)):   #answers 길이만큼 반복
        if answers[i] == a[i%len(a)]:   #a,b,c값이 반복되기 때문에 나머지(%) 사용
            cnt[0] += 1                 #답이 맞으면 count +1
        if answers[i] == b[i%len(b)]:
            cnt[1] += 1
        if answers[i] == c[i%len(c)]:
            cnt[2] += 1
    res = []    #결과를 담을 리스트
    for i in range(len(cnt)):   #cnt길이만큼 반복
        if cnt[i] == max(cnt):  #cnt[i]값과 cnt최댓값이 같으면 res에 추가
            res.append(i+1)
    return res