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

    # 그래프 구성
    for _ in range(edge):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # DFS 출력
    for i in DFS(graph, start):
        print(i, end=" ")

    print()

    # BFS 출력
    for i in BFS(graph, start):
        print(i, end=" ")
    

def DFS(graph, start):
    # 그래프 복사 후 역순 정렬
    g = [sorted(neigh, reverse=True) for neigh in graph]

    stack = [start]
    visited = [False] * len(graph)
    order = []
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            order.append(node)

            for nxt in g[node]:
                if not visited[nxt]:
                    stack.append(nxt)
    
    return order

def BFS(graph, start):
    g = [sorted(neigh) for neigh in graph]

    queue = deque([start])
    visited = [False] * len(graph)
    visited[start] = True
    order = [start]
    
    while queue:
        node = queue.popleft()

        for nxt in g[node]:
            if not visited[nxt]:
                visited[nxt] = True
                order.append(nxt)
                queue.append(nxt)
        
    return order


if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()