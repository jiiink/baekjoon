# 문제번호_제목.py
# url
# 알고리즘: 
# 핵심 아이디어: 

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main():
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    n = int(input().strip())

    # 한 줄에 여러 정수
    arr = list(map(int, input().split()))

    # 문자열
    s = input().strip()

    # --------------------------------------------

    # 문제 풀이 로직 작성 -------------------------
    result = sum(arr) + n
    print(result)
    # --------------------------------------------

def solve():
    # 여기에 풀이 로직 작성
    return

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()