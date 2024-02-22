import sys

N, M = map(int, sys.stdin.readline().split())
L = set() #set의 특징: 중복 허용 x, 인덱싱 없음
S = set()
for _ in range(N):
    name = input()
    L.add(name) #append 대신 add 사용

for _ in range(M):
    name = input()
    S.add(name)
    
same = sorted(list(L&S)) #교집합(&)사용해서 비교 후 list로 한 후 정렬
print(len(same))
for i in same:
    print(i)
