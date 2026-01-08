# 1463_1로 만들기.py
# https://www.acmicpc.net/problem/1463
# 알고리즘: 
# 핵심 아이디어: 

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main(): 
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    N = int(input().strip())
 
    # print(N)

    result = solve(N)
    print(result)

def solve(N):
    """
    보통 dp[] 를 정답으로 출력하니까, dp[] 에 결국 연산의 최소 횟수가 들어가게됨.
    dp[i] : i를 1로 만드는 데 필요한 최소 연산 횟수

    dp[0] = 0
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    dp[4] = 1 + dp[2] = 2
    dp[5] = dp[4] + 1 = 3
    dp[6] = 2
    dp[12] = 
    dp[n] = dp[n-1] + 1

    """

    dp = [0] * (N+1)
    # print(dp)
    for i in range(2, N+1):
        dp[i] = dp[i-1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)

    return dp[N]

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()