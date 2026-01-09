# 1654_랜선 자르기.py
# https://www.acmicpc.net/problem/1654
# 알고리즘: 
# 핵심 아이디어: 길이를 답 후보로 두고, 그 길이가 가능한지 검사하면서 이진 탐색해라.

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def solve(arr_k, n):
    # 여기에 풀이 로직 작성
    """
    Docstring for solve
    
    :param arr_k: Description
    :param n: Description

    length of lan cable: l
    sum(arr_k[] // l ) => n

    k 중 제일 작은 거를 처음 l로 하구, n 충족
    할 때까지 l을 줄이면 안 되나..?
    """
    left = 1
    right = max(arr_k)
    # length = min(arr_k) + 1
    # print(length)
    result = 0

    while left <= right:
        mid = (left + right) // 2

        count = sum([k//mid for k in arr_k])

        if count < n:
            right = mid - 1
        else:
            left = mid + 1

    return right

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    k, n = map(int, input().split())
    # print(k, n)
    arr_k = [int(input().strip()) for _ in range(k)]
    # print(arr_k)
    print(solve(arr_k, n))