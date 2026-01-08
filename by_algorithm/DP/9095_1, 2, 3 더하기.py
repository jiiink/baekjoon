# 9095_1, 2, 3 더하기.py
# https://www.acmicpc.net/problem/9095
# 알고리즘: dp
# 핵심 아이디어: "조합/순서 포함" 문제의 누적 규칙

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main(): 
    
    n = int(input().strip())
 
    testcases = [int(input().strip()) for _ in range(n)]

    # print(testcase)
    for testcase in testcases:
        print(solve(testcase))
    
def solve(n):
    """
    n 을 만드는 방법
    n-1 에서 +1
    n-2 에서 +2
    n-3 에서 +3

    =>dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

    기본값
    dp[1] = 1  # (1)
    dp[2] = 2  # (1+1), (2)
    dp[3] = 4  # (1+1+1), (1+2), (2+1), (3)
    """

    dp = [0] * (n+1)
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        return dp[n]




if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()