# 2751_수 정렬하기2.py
# https://www.acmicpc.net/problem/2751
# 알고리즘: 
# 핵심 아이디어: 

import sys
input = sys.stdin.readline

def main():
    n = int(input().strip())

    arr = [int(input().strip()) for i in range(n)]

    result = solve(arr)
    for num in result:
        print(num)

def solve(arr):
    return sorted(arr)

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()