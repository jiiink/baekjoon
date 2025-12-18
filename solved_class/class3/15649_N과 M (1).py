# 15649_N과 M (1).py
# https://www.acmicpc.net/problem/15649
# 알고리즘: backtracking
# 핵심 아이디어: 

import sys
from itertools import combinations

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

"""
백트래킹(Backtracking)이란?

가능한 모든 경우를 탐색하되,
더 이상 정답이 될 수 없는 경우는 즉시 되돌아가는(Pruning) 방법

---
🔍 구조를 분해해보면

백트래킹에는 항상 이 4가지가 있습니다:

1️⃣ 상태(State)
지금까지 선택한 것들
path = [1, 3]

2️⃣ 선택(Choice)
다음에 뭘 고를 수 있는가?
for i in range(1, N+1):

3️⃣ 제약(Constraint)
이 선택이 가능한가?
if not used[i]:

4️⃣ 종료 조건(Base Case)
언제 답으로 인정할 것인가?
if len(path) == M:

---
아래 문구가 보이면 백트래킹을 의심하세요:

“모든 경우 출력”

“조합 / 순열”

“중복 없이 선택”

“조건을 만족하는 경우의 수”

N ≤ 10, 15 정도
"""



    
def backtrack():
    if len(path) == M:
        print(*path)
        return
    
    for i in range(1, N + 1):
        print(path)
        if not used[i]:
            path.append(i)
            used[i] = True
            print(used)

            backtrack()

            path.pop()
            used[i] = False
            print(used)



if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    N, M = map(int, input().split())

    used = [False] * (N + 1)
    path = []

    backtrack()
    # main()