# 9663_N-Queen.py
# https://www.acmicpc.net/problem/9663
# 알고리즘: DFS, Backtracking
# 핵심 아이디어: 

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

N = int(input().strip())

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
            diag1[row - c] = True
            diag2[row + c] = True

            dfs(row + 1)

            col[c] = False
            diag1[row - c] = False
            diag2[row + c] = False

dfs(0)

print(answer)