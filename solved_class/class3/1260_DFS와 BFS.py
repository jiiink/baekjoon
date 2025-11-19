# 1260_DFS와 BFS.py
# https://www.acmicpc.net/problem/1260
# 알고리즘: DFS / BFS
# 핵심 아이디어: 그래프 저장 방식

import sys
from collections import deque

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline


def main(): 

    vertex, edge, start = map(int, input().split())
    graph = [[] for _ in range(vertex+1)]

    for _ in range(edge):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    
    for i in DFS(graph, start):
        print(i, end=" ")


    print()
    for i in BFS(graph, start):
        print(i, end=" ")
    
    

    
 

def DFS(graph, start):
    
    for index in range(1, len(graph)):
        graph[index].sort(reverse=True)
    stack = []
    
    visited = [start]
    

    for node in graph[start]:
        stack.append(node)
    
    
    while stack != []:
        popped = stack.pop()
        if popped not in visited:
            visited.append(popped)

        for node in graph[popped]:
            if node not in visited:
                stack.append(node)
    
    return visited

def BFS(graph, start):
    
    for index in range(1, len(graph)):
        graph[index].sort(reverse=False)

    queue = deque()
    visited = [start]
    
    for node in graph[start]:
        queue.append(node)
    
    
    while len(queue) != 0:
        popped = queue.popleft()
        if popped not in visited:
            visited.append(popped)
            
        
        for node in graph[popped]:
            if node not in visited:
                queue.append(node)
        
        
        
    return visited

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()