#DFS 메서드 정의
def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v] = True
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

computer = int(input())
pair = int(input())
graph = [[] * i for i in range(computer + 1)]
count = 0

for _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * (computer + 1)

#정의된 DFS 함수 호출
dfs(graph, 1, visited)
for i in range(1, len(visited)):
    if visited[i] == True:
        count += 1

print(count - 1) #1번 컴퓨터 빼기
