N = int(input())
data = list(map(int, input().split()))
count = 0

for num in data:
    for i in range(2, num + 1):
        if num % i == 0:
            if i == num:
                count += 1
            break #break를 넣고 안넣고가 다르다 왜...?

print(count)
