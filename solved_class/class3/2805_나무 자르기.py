# 2805_나무 자르기.py
# https://www.acmicpc.net/problem/2805
# 알고리즘: 
# 핵심 아이디어: 
"""

[1] input
[2] h 를 찾는 binary search
    left = 0
    right = max(trees)
    mid = 0
    while left <= right
        mid = (left + right) // 2

        length = trees - mid   # 음수면 0으로 취급
        total = length 들의 합

        if total < M
            right = mid - 1
        else
            left = mid + 1

    return right  # height

[3] height 출력

"""

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def binary_search(trees, M):
    # 여기에 풀이 로직 작성
    left = 0
    right = max(trees)
    height = 0

    while left <= right:
        mid = (left + right) // 2

        total = sum([tree-mid if tree-mid >= 0 else 0 for tree in trees])

        if total < M:
            right = mid - 1
        else:
            height = mid
            left = mid + 1
        

    # print(f'left: {left}, mid: {mid}, right: {right}')
    return height

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    N, M = map(int, input().split())
 
    trees = list(map(int, input().split()))

    print(binary_search(trees, M))

    # print(N, M, trees)