# 9012_괄호.py
# https://www.acmicpc.net/problem/9012
# 알고리즘: 
# 핵심 아이디어: stack

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main(): 

    n = int(input().strip())

    parenthesis_stack = []
 
    answer = []

    # c = input().split()

    # print(c)

    for _ in range(n):
        parenthesis_stack = []
        ps = input().strip()
        # print(ps)
        for p in ps:
            if p == "(":
                parenthesis_stack.append(p)
            elif p == ")":
                if not parenthesis_stack:
                    parenthesis_stack.append(0)
                    break
                parenthesis_stack.pop()
            # print(f'stack: {parenthesis_stack}')
        if not parenthesis_stack:
            answer.append("YES")
        else:
            answer.append("NO")
        # print(f'answer: {answer}')


    # print(answer)
    for a in answer:
        print(a)
        

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()