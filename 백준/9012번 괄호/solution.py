T = int(input()) #입력 데이터의 수 정수 T

for i in range(T):
    PS = str(input()) #문자열 PS를 받는다
    x = 0
    if len(PS) < 2 or len(PS) > 50: #문자열 길이 제한
        print("Incorrect")
        
    for j in range(len(PS)):
        if PS[j] == '(': #'(' 일 때 x를 +1 해줌
            x += 1
        elif PS[j] == ')': #')' 일 때 x를 -1 해줌
            x -= 1
        if x < 0: 
            #만약 x가 음수가 될 경우 문자열이 ')'부터 시작하므로 올바르지 않음
            x = -1 # x가 0이 안되게 만듬
            break
    if x == 0: # x가 0이면 '(' 과 ')'의 개수가 일치함
        print("YES")
    else:
        print("NO")
