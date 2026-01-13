# 2178_미로 탐색.py
# https://www.acmicpc.net/problem/2178
# 알고리즘: 
# 핵심 아이디어: 

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline


def bfs(maze):
    from collections import deque
    queue = deque()
    queue.append((0, 0))

    dx = [-1, +1,  0,  0]
    dy = [0 ,  0, -1, +1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 체크
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[N-1][M-1]

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    N, M = map(int, input().split())

    # print(n, m)
    maze = [list(map(int, input().strip())) for _ in range(N)]

    # print(maze)

    print(bfs(maze))