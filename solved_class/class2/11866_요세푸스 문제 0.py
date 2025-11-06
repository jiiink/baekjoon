# 11866_요세푸스 문제 0.py
# https://www.acmicpc.net/problem/11866
# 알고리즘: 
# 핵심 아이디어: 

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())

    # slow(N, K)
    fast(N, K)


def fast(N, K):
    people = list(range(1, N+1))
    out = []
    index = 0

    while people:
        index = (index + K - 1) % len(people)
        out.append(people.pop(index))

    print("<" + ", ".join(map(str, out)) + ">")
    


def slow(N, K):
    # print(f'{N}, {K}')
    table = [[x+1, 0] for x in range(N)]

    # print(table)
    count = 0
    i = -1
    rejected = []
    while len(rejected) != N:
        count = 0
        while count != K:
            i = (i + 1) % N
            if (table[i][1] == 0):
                count += 1
            

        rejected.append(table[i][0])
        table[i][1] = 1

    rejected_print(rejected)


def rejected_print(rejected):
    print('<', end='')
    for x in range(len(rejected) - 1):
        print(f'{rejected[x]}, ', end='')
    print(f'{rejected[-1]}>')


if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()

