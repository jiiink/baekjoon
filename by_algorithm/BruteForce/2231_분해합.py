# 2231_분해합.py
# https://www.acmicpc.net/problem/2231
# 알고리즘: brute force
# 핵심 아이디어: 완전 탐색할 때 범위 선정

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main():
    target_number = input().strip()
    
    # --------------------------------------------
    result = solve(target_number, len(target_number))
    print(result)
    # --------------------------------------------

def solve(target_number: str, digit_length: int) -> int:
    # 여기에 풀이 로직 작성
    result = 0
    target = int(target_number)

    min_candidate = target - 9 * digit_length

    for candidate in range(max(1, min_candidate), target):
        if (calculate_decomposition_sum(candidate) == target):
            return candidate

    return result

def calculate_decomposition_sum(number: int) -> int:
    number_str = str(number)
    digit_sum = sum(int(digit) for digit in number_str)
    return number + digit_sum


if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()