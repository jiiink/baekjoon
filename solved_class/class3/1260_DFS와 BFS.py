# 1260_DFS와 BFS.py
# https://www.acmicpc.net/problem/1260
# 알고리즘: 
# 핵심 아이디어: 그래프 저장 방식 / DFS / BFS

import sys
from collections import deque

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

# graph = [[] for _ in range(N+1)]
"""
graph[0] = []
graph[1] = [ ... ] 1번 노드에 연결된 노드들
"""

def main(): 
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    vertex, edge, start = map(int, input().split())
    graph = [[] for _ in range(vertex+1)]

    for _ in range(edge):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # print(vertex, edge, start)
    # print(graph)
    

    # print(graph)
    # print(DFS(graph, start))
    for i in DFS(graph, start):
        print()
    print(BFS(graph, start))
    

    
 

def DFS(graph, start):
    # 여기에 풀이 로직 작성
    for index in range(1, len(graph)):
        graph[index].sort(reverse=True)
    stack = []
    # stack.append()
    visited = [start]
    

    for node in graph[start]:
        stack.append(node)
    
    # print(stack)

    while stack != []:
        popped = stack.pop()
        if popped not in visited:
            visited.append(popped)
        # print(visited)

        for node in graph[popped]:
            if node not in visited:
                stack.append(node)
    # print(visited)
    return visited

def BFS(graph, start):
    # 여기에 풀이 로직 작성
    for index in range(1, len(graph)):
        graph[index].sort(reverse=False)

    queue = deque()
    visited = [start]
    
    for node in graph[start]:
        queue.append(node)
    
    # print(queue)
    while len(queue) != 0:
        popped = queue.popleft()
        if popped not in visited:
            visited.append(popped)
            # print(visited)
        
        for node in graph[popped]:
            if node not in visited:
                queue.append(node)
        
        # print(queue)

        
        
    return visited

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()