# 10818_최소, 최대.py
# https://www.acmicpc.net/problem/10818
# 알고리즘: 
# 핵심 아이디어: 

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main():

    n = int(input().strip())

    arr = list(map(int, input().split()))

    print(f'{min(arr)} {max(arr)}')


def solve():
    # 여기에 풀이 로직 작성
    return

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()