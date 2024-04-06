import sys

N, K = map(int, sys.stdin.readline().split())

bag = [[]*i for i in range(2)]
for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    bag[0].append(W)
    bag[1].append(V)

# 인덱스는 0번부터 시작이기에 숫자를 정수로 맞추기 위해 +1씩 더함
array = [[0]*(N+1) for _ in range(K+1)]

'''
2차원 DP > 기준점을 2개로 잡음
=> 점화식을 2개로 만듬
1) 현재 배낭 허용무게보다 크면 담지 않는다
2) 더 높은 가치를 선택한다
    - 현재의 아이템을 넘겼을때의 가치
    - 현재의 아이템을 담을 수 있었을 때 + 현재를 담았을 때 가치

사실 잘 모르겠다....
'''

for i in range(1, K+1):
    for j in range(1,N+1):
        weight = bag[0][j-1]
        value = bag[1][j-1]

        if i < weight:
            array[i][j] = array[i][j-1]
        else:
            array[i][j] = max(array[i][j-1], array[i-weight][j-1]+value)

print(array[K][N])
