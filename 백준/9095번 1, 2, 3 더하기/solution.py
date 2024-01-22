T = int(input())

d = [0]*11
d[0] = 1
d[1] = 2
d[2] = 4
for i in range(3,11):
    d[i] = d[i-1] + d[i-2] + d[i-3]

N = [0]*T
for j in range(T):
    N[j] = int(input())
    print(d[N[j]-1])
