# 2110_공유기 설치.py
# https://www.acmicpc.net/problem/2110
# 알고리즘: 
# 핵심 아이디어: 

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def solve(N, C, houses):
    # 여기에 풀이 로직 작성
    left = 1
    right = houses[-1] - houses[0]
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        last = houses[0]
        count = 1

        for i in range(1, N):
            if houses[i] - last >= mid:
                count += 1
                last = houses[i]

        if count >= C:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    N, C = map(int, input().split())

    houses = [int(input().strip()) for _ in range(N)]

    # print(houses)
    houses.sort()
    # print(houses)
    print(solve(N, C, houses))
