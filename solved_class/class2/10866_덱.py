# 10866_덱.py
# https://www.acmicpc.net/problem/10866
# 알고리즘: 
# 핵심 아이디어: 

import sys
from collections import deque

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline
deque = deque()

def main():
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    n = int(input().strip())

    for _ in range(n):
        command = input().split()

        if command[0] == "push_front":
            deque.appendleft(int(command[1]))
        elif command[0] == "push_back":
            deque.append(int(command[1]))
        elif command[0] == "pop_front":
            print(deque.popleft() if deque else -1)
        elif command[0] == "pop_back":
            print(deque.pop() if deque else -1)
        elif command[0] == "size":
            print(len(deque))
        elif command[0] == "empty":
            print(1 if len(deque) == 0 else 0)
        elif command[0] == "front":
            print(deque[0] if deque else -1)
        elif command[0] == "back":
            print(deque[-1] if deque else -1)

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()