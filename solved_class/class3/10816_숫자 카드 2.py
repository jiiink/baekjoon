# 10816_숫자 카드 2.py
# https://www.acmicpc.net/problem/10816
# 알고리즘: 
# 핵심 아이디어: 해시, 이분탐색

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline


if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    N = int(input().strip())
    cards = list(map(int, input().split()))
    count = {}

    for num in cards:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    M = int(input().strip())
    # targets = [list(map(int ,input().split())) for _ in range(M)]
    queries = list(map(int, input().split()))
 
    # print(cards, targets)
    result = []
    for q in queries:
        result.append(str(count.get(q, 0)))

    print(*result, sep=" ")