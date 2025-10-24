# 10828_스택구현.py
# https://www.acmicpc.net/problem/10828
# 알고리즘: 
# 핵심 아이디어: 

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline


stack = []

def main():
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    n = int(input().strip())

    for i in range(n):
        command = input().split()
        # print(f"command: {command}")
        
        if command[0] == 'push':
            # push command[1]
            stack.append(int(command[1]))
        elif command[0] == 'top':
            # top
            if (len(stack) == 0):
                print(-1)
            else:
                print(stack[-1])
        elif command[0] == 'size':
            # size
            print(len(stack))
        elif command[0] == 'empty':
            # empty
            print(1 if (len(stack) == 0) else 0)
        elif command[0] == 'pop':
            # pop

            if (len(stack) == 0):
                print(-1)
            else:
                print(stack.pop(-1))


def solve():
    # 여기에 풀이 로직 작성
    
    return

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()