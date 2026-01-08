# 2606_바이러스.py
# https://www.acmicpc.net/problem/2606
# 알고리즘: 탐색
# 핵심 아이디어: 

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main(): 
    
    n = int(input().strip())
    network = [[] for _ in range(n+1)]
    # print(network)
    # print(len(network))
    
 
    edges = int(input().strip())
    
    for _ in range(edges):
        a, b = map(int, input().split())
        network[a].append(b)
        network[b].append(a)


    # print(network)
    visited = bfs(network)
    print(len(visited) - 1)


def bfs(network):
    from collections import deque

    start = 1
    queue = deque(network[start])
    visited = [1]

    while queue:
        # print(queue)
        # print(visited)
        popped = queue.popleft()

        if popped not in visited:
            visited.append(popped)
            for next in network[popped]:
                if next not in visited:
                    queue.append(next)
    # print(visited)
    return visited


if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()