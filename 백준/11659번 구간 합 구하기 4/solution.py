import sys

N, M = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))
sum = 0
sum_list = [] #누적합을 구하기 위한 list

for i in range(N):
    sum += sequence[i] #누적합을 구함
    sum_list.append(sum) #누적합을 list에 append

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1: # i==1이라면 index 0번이기 때문에
        print(sum_list[j-1]) #0번 index를 뺄 필요가 없음
    else: #index는 0부터 시작이므로 -1씩 해주고 i번째부터 더하기 때문에 -1을 함
        print(sum_list[j-1] - sum_list[i-2])
