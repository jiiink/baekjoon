# 10869_사칙연산.py
# https://www.acmicpc.net/problem/10869
# 알고리즘: 
# 핵심 아이디어: 

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main():
    a, b = map(int, input().split())

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)

def solve():
    # 여기에 풀이 로직 작성
    return

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()