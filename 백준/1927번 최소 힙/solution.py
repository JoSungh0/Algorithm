import heapq
import sys

heap = []

N = int(input())

for _ in range(N):
    i = int(sys.stdin.readline()) # int(input())으로 하면 시간 초과됨
    if i == 0:
        if len(heap) == 0: # heap배열 안에 아무 자연수도 없을 시
            print(0)
        else:
            print(heapq.heappop(heap)) # pop하면 알아서 최소값을 반환해준다
            
    else:
        heapq.heappush(heap, i) # heapq에 puth하는 방법
