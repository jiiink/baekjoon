# 2667_단지번호붙이기.py
# https://www.acmicpc.net/problem/2667
# 알고리즘: bfs
# 핵심 아이디어: 
"""
[1] 지도 입력 받기
[2] 지도의 처음부터 1을 탐색
    1을 찾은 그 지점부터 bfs()
        bfs 를 통해 인접한 1을 찾음
            탐색한 지점은 0 으로. (방문처리)
    탐색한 수를 return
[4] bfs() 에서 return 받은 값을 배열에 저장
[5] 배열을 오름차순 정렬
[6] 배열의 길이와 내용물 출력
"""

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline


def bfs(graph, start):
    # print(f'start : {start}')
    from collections import deque
    queue = deque()
    queue.append(start)
    graph[start[0]][start[1]] = 0
    count = 1

    dx = [-1, +1,  0,  0]
    dy = [0 ,  0, -1, +1]

    

    while queue:
        x, y = queue.popleft()

        for i in range(4):
        
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
            
    return count






if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    N = int(input().strip())
 
    graph = [list(map(int, input().strip())) for _ in range(N)]

    result = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                result.append(bfs(graph, (i, j)))
 
    result.sort()

    print(len(result))
    # for apt in result:
    #     print(apt)
    # print('\n'.join(map(str, result)))
    print(*result, sep='\n')