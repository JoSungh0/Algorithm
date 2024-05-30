def factorial(n): #팩토리얼 함수
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

N = int(input())

num = factorial(N)

tostr = str(num) #문자열로 바꿔서 각 숫자마다 접근 가능하게 함
count = 0

for i in range(len(tostr) - 1, -1, -1): #문자열을 반대부터 살펴봄
    if tostr[i] != '0': #0이 바로 나오면 멈춤
        break
    else:
        count += 1

print(count)
