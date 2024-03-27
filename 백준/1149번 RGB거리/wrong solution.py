import sys

N = int(sys.stdin.readline())
total = 0
RGB = list(map(int, sys.stdin.readline().split()))
total += min(RGB)
before = RGB.index(min(RGB))
for _ in range(N-1):
    RGB = list(map(int, sys.stdin.readline().split()))
    if before == RGB.index(min(RGB)):
        RGB[before] = 1001
        total += min(RGB)
        before = RGB.index(min(RGB))
    else:
        total += min(RGB)
        before = RGB.index(min(RGB))
    
print(total)
