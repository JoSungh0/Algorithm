N = int(input())

if N < 3 or N >5000:
    print('Can`t')
    
if N%5 == 0: # 1. 5kg로 나누어 떨어질 때
    print(N//5)
else:
    count = 0
    while N > 0:
        N -= 3
        count += 1
        if N % 5 == 0: # 2. 3kg와 5kg로 조합할 수 있을 때
            count += N // 5
            print(count)
            break
        elif N == 1 or N == 2: # 3. 설탕 봉지만으로 불가능
            print(-1)
            break
        elif N == 0: # 4. 3kg로 나누어 떨어질 때
            print(count)
            break
