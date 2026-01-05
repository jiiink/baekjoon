# 1012_유기농 배추.py
# https://www.acmicpc.net/problem/1012
# 알고리즘: 
# 핵심 아이디어: 

import sys
from collections import deque

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main(): 
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    T = int(input().strip())

    for _ in range(T):
        M, N, K = map(int, input().split())
        field = [[0]*M for _ in range(N)]

        # 배추 심기
        for _ in range(K):
            x, y = map(int, input().split())
            field[y][x] = 1

        count = 0

        for y in range(N):
            for x in range(M):
                if field[y][x] == 1: # 배추 그룹 발견
                    bfs(y, x, field, N, M)
                    count += 1

        print(count)
    


def bfs(start_y, start_x, field, N, M):

    queue = deque()
    queue.append((start_y, start_x))
    field[start_y][start_x] = 0 # 방문처리

    dx = [1, -1, 0,  0]
    dy = [0,  0, 1, -1]

    while queue:
        y, x = queue.popleft()

        for i in range(4): # 상하좌우 인접한 노드 큐에 넣기
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if field[ny][nx] == 1:
                    field[ny][nx] = 0
                    queue.append((ny, nx))




def print_field(field):
    for row in range(len(field)):
        print(field[row])
    
if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()