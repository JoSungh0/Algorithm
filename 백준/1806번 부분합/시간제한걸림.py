import sys

N, S = map(int, sys.stdin.readline().split())

seqeunce = list(map(int, sys.stdin.readline().split()))
if len(seqeunce) != N:
    print("false")
first = True
for n in range(N):
    i = len(seqeunce) - n
    for j in range(i):
        sum = 0
        for k in range(j, j+n):
            sum += seqeunce[k]
        if sum >= S:
            first = False
            print(n)
            break
    if first == False:
        break
if n == len(seqeunce):
    print(0)
