# 18258_큐구현.py
# https://www.acmicpc.net/problem/18258
# 알고리즘: 
# 핵심 아이디어: 시간초과 주의 (자료구조, 입출력)

import sys
from collections import deque

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline


def main():
    queue = deque()
    n = int(input().strip())

    for _ in range(n):
        command = ""
        command = input().split()

        if command[0] == 'push':
            queue.append(int(command[1]))
        elif command[0] == 'pop':
            print(queue.popleft() if queue else -1)
        elif command[0] == 'size':
            print(len(queue))
        elif command[0] == 'empty':
            print(0 if queue else 1)
        elif command[0] == 'front':
            print(queue[0] if queue else -1)
        elif command[0] == 'back':
            print(queue[-1] if queue else -1)


if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()


