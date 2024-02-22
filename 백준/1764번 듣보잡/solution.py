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

#####
#same = L.intersection(S) #교집합인 부분을 set으로
#same = list(same) #set-> list
#same.sort() #사전순 출력을 위해
#####
