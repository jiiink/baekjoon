# 11726_2×n 타일링.py
# https://www.acmicpc.net/problem/11726
# 알고리즘: 
# 핵심 아이디어: 

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main(): 
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    n = int(input().strip())
 
    print(solve(n)%10007)

def solve(n):
    # 여기에 풀이 로직 작성
    """
    1단계. DP 정의부터 먼저 만든다
        dp[i] = 2 x i 를 채우는 방법 수
    2단계. "i로 오기 직전 상황"을 생각한다
        dp[i-1] 에서 세로 막대 하나
        dp[i-2] 에서 가로 막대 둘
    3단계. 점화식 세우기
        dp[i] = dp[i-1] + dp[i-2]
    4단계. 초기값 먼저 채운다
        dp[1] = 1
        dp[2] = 2
    """

    dp = [0] * (n + 1)
    
    for i in range(1, n+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        else:
            dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()