# 1541_잃어버린 괄호.py
# https://www.acmicpc.net/problem/1541
# 알고리즘: 
# 핵심 아이디어: 

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def solve():
    # 여기에 풀이 로직 작성
    expr = input().strip()
    parts = expr.split('-')

    result = sum(map(int, parts[0].split('+')))
    
    for part in parts[1:]:
        result -= sum(map(int, part.split('+')))

    print(result)

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    solve()