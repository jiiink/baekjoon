# 2579_계단 오르기.py
# https://www.acmicpc.net/problem/2579
# 알고리즘: DP
# 핵심 아이디어: 연속해서 3개의 계단을 밟을 수 없다는 규칙을 DP로 표현

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main(): 
    
    n = int(input().strip())

    stair = []
    stair.append(0)
 
    for _ in range(n):
        score = int(input().strip())
        stair.append(score)

    dp = up(n, stair)
    print(dp[n])


def up(n, stair):
    """
    dp[i] : i번째 계단에서의 최대 점수

    계단을 연속 3개 오르면 안 되는 규칙 표현
    dp[i] = max(dp[i-3] + stair[i-1] + stair[i], 
                   dp[i-2] + stair[i])

    계단이 1, 2, 3개일 때는 따로 설정
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]
    dp[3] = max(stair[1] + stair[3], stair[2] + stair[3])
    """
    
    dp = [0] * (n+1)

    # print(dp)
    for i in range(1, n+1):
        if i == 1:
            dp[i] = stair[i]
        elif i == 2:
            dp[i] = stair[i-1] + stair[i]
        elif i == 3:
            dp[i] = max(stair[i-2] + stair[i], stair[i-1] + stair[i])
        else:
            dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

    return dp

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()