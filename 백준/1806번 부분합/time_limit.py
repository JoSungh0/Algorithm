import sys

N, S = map(int, sys.stdin.readline().split())

sequence = list(map(int, sys.stdin.readline().split()))
if len(sequence) != N:
    print("false")
first = True
for n in range(N):
    i = len(sequence) - n
    for j in range(i):
        sum = 0
        for k in range(j, j+n):
            sum += sequence[k]
        if sum >= S:
            first = False
            print(n)
            break
    if first == False:
        break
if n == len(sequence):
    print(0)
