import sys
from collections import deque # queue 자료구조를 사용하기 위함
# queue 자료구조를 사용할 때 list보다 deque가 연산속도가 압도적으로 빠르다.

# 정점 개수 N, 간선 개수 M, 시작 정점번호 V
N, M, V = map(int, sys.stdin.readline().split())

# 정점 간의 연결을 저장
tree = [[]*(N+1) for _ in range(N+1)] # 1번부터 시작이므로 N+1

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    # 각 정점에 서로의 정점을 넣어 연결해줌
    tree[a].append(b)
    tree[b].append(a)
    # append는 정렬 상관 없이 넣기 때문에 sort()로 정렬
    tree[a].sort()
    tree[b].sort()

# DFS 알고리즘
'''
재귀 형식으로 방문함
1) 해당 정점의 방문 기록 확인
2) 방문 기록이 없다면 바로 그 정점으로 들어감
3) 들어간 정점에서 다시 방문 기록 확인
4) 위의 과정을 반복해서 깊이 탐색
'''
visted1 = [False]*(N+1) # 정점의 방문 기록

def DFS(V, visted):
    visted[V] = True # 시작 정점을 방문으로 표시
    
    print(V, end=" ") # 방문한 정점 출력

    for i in tree[V]: # 해당 정점의 tree 연결을 봄
        if not visted[i]: # 방문 기록에서 해당 정점을 방문하지 않았으면 방문하러 감
            DFS(i, visted) # 재귀형식으로 해서 새로운 정점을 탐색함


# BFS 알고리즘
'''
Queue 자료구조를 활용함
1) 해당 정점의 방문 기록 확인
2) 방문 기록이 없다면 우선 Queue에 저장한 이후
현재 정점과 연결된 다른 정점의 방문기록 계속 확인
3) Queue.pop 한 정점으로 위의 과정 반복
4) Queue 안에 아무 정점도 없으면 종료
'''
visted2 = [False]*(N+1) # 정점의 방문 기록

def BFS(V, visted):
    queue = deque([V]) # queue 자료구조 사용
    visted[V] = True # 시작 정점을 방문으로 표시
    
    while queue: # queue안의 데이터가 없으면 종료
        V = queue.popleft() # queue.pop()
        
        print(V, end=" ") # 방문한 정점 출력

        for i in tree[V]: # 현재 정점의 tree 연결 확인
            if not visted[i]: # 방문 기록에 해당 정점이 없다면
                queue.append(i) # queue에 저장
                visted[i] = True # 해당 정점을 방문으로 표시
                # 이후에 현재 정점의 tree연결을 계속 확인함

DFS(V, visted1)
print() 
BFS(V, visted2)
