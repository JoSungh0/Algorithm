import sys

sequence = list(map(int, sys.stdin.readline().split()))
percent = [[0 for _ in range(8)] for _ in range(8)] #각 항목에 대해 이기는 전체 percent를 구하기 위함
index = 0
for i in range(8):
    for j in range(i+1, 8):
        percent[i][j] = round(sequence[index]/100, 9) #percent array에 입력받은 win percent가 들어감
        percent[j][i] = round(abs(100 - sequence[index])/100, 9) #array에 반대가 이기는 percent를 계산해서 입력
        index += 1

#percent array에서 round에 쓰이는 순서
'''
0:  x 1 2 2 3 3 3 3
1:  1 x 2 2 3 3 3 3
2:  2 2 x 1 3 3 3 3
3:  2 2 1 x 3 3 3 3
4:  3 3 3 3 x 1 2 2
5:  3 3 3 3 1 x 2 2
6:  3 3 3 3 2 2 x 1
7:  3 3 3 3 2 2 1 x
'''
first = [0 for _ in range(8)] #첫번째 round
for i in range(8):
    if i%2 == 0: #짝수일 때 홀수 번이 win percent
        first[i] = percent[i][i+1]
    else: #홀수일 땐 반대
        first[i] = percent[i][i-1]

second = [0 for _ in range(8)]
for i in range(8): #내가 전 상대를 이긴 확률 * (현재의 상대 이길 수 있는 확률 * 상대방이 전 상대를 이긴 확률)
    if i%4 == 0:
        second[i] = first[i] * (first[i+2] * percent[i][i+2] + first[i+3] * percent[i][i+3])
    elif i%4 == 1:
        second[i] = first[i] * (first[i+1] * percent[i][i+1] + first[i+2] * percent[i][i+2])
    elif i%4 == 2:
        second[i] = first[i] * (first[i-2] * percent[i][i-2] + first[i-1] * percent[i][i-1])
    elif i%4 == 3:
        second[i] = first[i] * (first[i-3] * percent[i][i-3] + first[i-2] * percent[i][i-2])

final = [0 for _ in range(8)]
for i in range(8):
    if i < 4: #내가 전 상대를 이긴 확률 * (현재의 상대 이길 수 있는 확률 * 상대방이 전 상대를 이긴 확률)
        final[i] = second[i] * (second[4] * percent[i][4] + second[5] * percent[i][5] + second[6] * percent[i][6] + second[7] * percent[i][7])
    else:
        final[i] = second[i] * (second[0] * percent[i][0] + second[1] * percent[i][1] + second[2] * percent[i][2] + second[3] * percent[i][3])

print(" ".join(str(i) for i in final))
