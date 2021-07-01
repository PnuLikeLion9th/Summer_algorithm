h,m = input().split()
m = int(m) - 45  # 입력받은 m에서 45빼기
if m<0:          # m이 음수라면
    h= int(h)-1  # 1시간 감소시키고,
    m = m+60     # m에 60 더함
if h<0:          # h가 음수가 된다면, ex) 0:30인 경우 45뺐을 때 h=-1이 됨
    h = h+24     # h에 24 더함  => ex) 23:@@이 됨
print(h,m)