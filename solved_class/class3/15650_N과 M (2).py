# 15650_N과 M (2).py
# https://www.acmicpc.net/problem/15650
# 알고리즘: 
# 핵심 아이디어: 

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def backtracking(start, path):
    # 여기에 풀이 로직 작성
    # print(f'in backtracking path: {path}')
    if len(path) == M:
        print(*path)
        return
    
    for i in range(start, N+1):
            # print(f'i: {i}, start: {start}')
            path.append(i)
            # used[i] = True

            backtracking(i + 1, path)

            path.pop()
            # used[i] = False

    # path.pop()
    # print("cycle end")
    return



if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    N, M = map(int, input().split())
 
    path = []
    start = 1
    backtracking(start, path)