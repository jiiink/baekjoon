# 1931_회의실 배정.py
# https://www.acmicpc.net/problem/1931
# 알고리즘: 
# 핵심 아이디어: 끝나는 시간 기준 오름차순 정렬

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main(): 

    meetings = []

    N = int(input())
 
    for _ in range(N):
        start, end = map(int, input().split())
        meetings.append((start, end))

    # print(seminars)

    meetings.sort(key=lambda x: (x[1], x[0]))

    # print(meetings)

    accepted = []

    j = 0
    for i in range(len(meetings)):
        if accepted == []:
            accepted.append(meetings[i])
        elif meetings[i][0] >= accepted[j][1]:
            accepted.append(meetings[i])
            j += 1

    # print(accepted)
    print(len(accepted))

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()