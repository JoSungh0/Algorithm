import sys

N, S = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0 #포인터 두개 만듬
result = 100000 # N의 최대길이
sum = sequence[0]
while True:
    if sum < S: # S가 sum보다 크면
        # right +1 하고 sum에 값 추가
        right += 1
        if right == N: break #만약 right가 인덱스 끝에 닿았으면 종료
        sum += sequence[right]
        
    else: # sum이 S 이상이면
        # S가 이상일 때의 길이 저장 및 최저 길이랑 비교
        # sum에서 left꺼 빼고 left +1
        result = min(result, right - left + 1) # index가 0부터 시작이므로 +1
        sum -= sequence[left]
        left += 1
# sum이 S보다 큰것이 한개도 없으면 result는 N의 최대길이
print(0 if result == 100000 else result) 
