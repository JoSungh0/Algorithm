import sys
sys.setrecursionlimit(10**7) # 시스템의 안정을 위한 재귀 한도를 늘려줌

A, B, C = map(int, sys.stdin.readline().split())

'''
a**8 = a*a*a*a*a*a*a*a > 연산을 8번 해줘야 함
     = ((a**2)**2)**2 > 연산을 3번

     => (a**(b/2))**2를 반복함
재귀를 이용해 재귀 횟수를 줄임
'''
def multiple(A, B, C): 
    if B == 0: # A**0 일 때 1을 반환
        return 1
    
    temp = multiple(A, B//2, C) # A**(B//2)를 반복
    temp = (temp * temp) # A**(B//2)에 **2를 곱해줌
    
    if B%2 == 0: 
        return temp%C # 나머지 계산
    else: # B가 홀수일 경우 A값을 한번 더 곱해줘야 함 ex) 2^3 = 2^2 * 2
        return (temp*A)%C
    
result = multiple(A, B, C)
print(result)
