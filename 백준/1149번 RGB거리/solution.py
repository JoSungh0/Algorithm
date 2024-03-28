import sys

N = int(sys.stdin.readline())

RGB = [[0]*3 for _ in range(N)] # RGB거리 배열을 만듬

for i in range(N):
   RGB[i] = list(map(int, sys.stdin.readline().split()))

# R일 때 그 전의 G, B의 값 중 최소값을 더하고 마찬가지로 G, B도 똑같이
for i in range(1,N): 
   RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0]
   RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1]
   RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1]) + RGB[i][2]

print(min(RGB[-1][0], RGB[-1][1], RGB[-1][2])) #R, G, B 중에서의 최소값을 출력한다
