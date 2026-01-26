# 9663_N-Queen.py
# https://www.acmicpc.net/problem/9663
# 알고리즘: DFS, Backtracking
# 핵심 아이디어: 

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

N = int(input().strip())

"""
Queen 위치 판단 조건
열 
대각선(왼쪽 위) : 이전에 놓은 퀸의 자리
대각선(오른쪽 아래) : 앞으로 놓을 퀸은 여기 있으면 안 됨
"""

col = [False] * N
diag1 = [False] * (2 * N)
diag2 = [False] * (2 * N)

answer = 0

def dfs(row):
    global answer
    
    if row == N:
        answer += 1
        return
    
    for c in range(N):
        if not col[c] and not diag1[row-c] and not diag2[row+c]:
            col[c] = True
            diag1[row-c] = True
            diag2[row+c] = True

            dfs(row + 1) # 다음 행에 퀸 놓을 자리 탐색

            # 새로운 경우를 위한 원상회귀 Backtracking
            col[c] = False
            diag1[row-c] = False
            diag2[row+c] = False

dfs(0)
print(answer)