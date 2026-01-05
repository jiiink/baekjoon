# 9012_괄호.py
# https://www.acmicpc.net/problem/9012
# 알고리즘: 
# 핵심 아이디어: stack

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main(): 

    n = int(input().strip())

    for _ in range(n):
        string = input().strip()
        print(isVPS(string))

def isVPS(string):
    stack = []
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return "NO"
            stack.pop()

    return "YES" if not stack else "NO"
        

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()