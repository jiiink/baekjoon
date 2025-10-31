# 10814_나이순 정렬.py
# https://www.acmicpc.net/problem/10814
# 알고리즘: 
# 핵심 아이디어: 여러 조건의 정렬

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main():
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    members = []
    n = int(input().strip())

    for i in range(n):
        age, name = input().split()
        members.append([int(age), name, i])

    # print(people)

    members.sort(key=lambda x: (x[0], x[2]))

    for member in members:
        print(member[0], member[1])


if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()