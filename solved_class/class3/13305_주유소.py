# 13305_주유소.py
# https://www.acmicpc.net/problem/13305
# 알고리즘: 
# 핵심 아이디어: 

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def solve(distances, prices):
    # 여기에 풀이 로직 작성

    min_price = prices[0]
    total_price = 0

    for i in range(0, len(prices)-1):
        total_price += min_price * distances[i]
        if min_price > prices[i+1]:
            min_price = prices[i+1]

    return total_price

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    N = int(input().strip())
 
    # 한 줄에 여러 정수
    distances = list(map(int, input().split()))

    prices = list(map(int, input().split()))

    print(solve(distances, prices))