# 9498_시험성적.py
# https://www.acmicpc.net/problem/9498
# 알고리즘: 
# 핵심 아이디어: if - elif 조건문

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main():
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    n = int(input().strip())

    grade = ""
    if (n >= 90):
        grade = 'A'
    elif (n >= 80):
        grade = 'B'
    elif (n >= 70):
        grade = 'C'
    elif (n >= 60):
        grade = 'D'
    else:
        grade = 'F'

    print(grade)

def solve():
    # 여기에 풀이 로직 작성
    return

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()