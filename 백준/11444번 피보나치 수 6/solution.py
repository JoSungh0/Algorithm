'''
피보나치 점화식
f[2n] = f[n//2 + 1]^2 - f[n//2 - 1]^2
f[2n-1] = f[n//2 + 1]^2 + f[n//2]^2
'''

mem = {} #dictionary 자료형을 사용해서 필요한 숫자만 접근하면 되기때문에 메모리를 더 줄일 수 있음

def fibo(n):
    if mem.get(n) != None: #메모이제이션 활용
        return mem[n]
    
    if n == 0: #0이면 0반환
        return 0
    
    if n == 1 or n == 2: #1,2면 1반환
        return 1
    
    if n%2 == 0: #짝수면 f[n//2 + 1]^2 - f[n//2 - 1]^2을 반환한다
        mem[n//2 + 1] = fibo(n//2 + 1) % 1000000007
        mem[n//2 - 1] = fibo(n//2 - 1) % 1000000007
        return mem[n//2 + 1]**2 - mem[n//2 - 1]**2
    
    else: #홀수면 f[n//2 + 1]^2 + f[n//2]^2을 반환한다
        mem[n//2 + 1] = fibo(n//2 + 1) % 1000000007
        mem[n//2] = fibo(n//2) % 1000000007
        return mem[n//2 + 1]**2 + mem[n//2]**2
    
N = int(input())
result = fibo(N) % 1000000007
print(result)
