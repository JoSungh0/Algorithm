'''
문제 딱 봤을 때 그냥 탐색으로 대충 하면 될 줄 알았는데
1000000000000000000같이 이렇게 큰 수는 메모리가 부족함
그래서 안됨
'''
array = [0] * 1000000000000000000
array[0] = [0]
array[1] = [1]

for i in range(2, 1000000000000000001):
    array[i] = array[i-1] + array[i-2]
    
N = int(input())
result = array[N] % 1000000007
print(result)
