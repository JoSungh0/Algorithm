import sys

people = int(sys.stdin.readline())
time = []
last = 0
time = list(map(int, sys.stdin.readline().split()))
time.sort()
for i in range(people):
    last += time[i]
    time[i] = last
print(sum(time))
