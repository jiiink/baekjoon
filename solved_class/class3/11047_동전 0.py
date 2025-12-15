# 11047_동전 0.py
# https://www.acmicpc.net/problem/11047
# 알고리즘: greedy
# 핵심 아이디어: 큰 동전부터

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main(): 

    n, k = map(int, input().split())

    coins = [int(input().strip()) for _ in range(n)]

    """
    그리디

    이 문제는 큰 동전이 항상 작은 동전 여러 개보다 
    효율적이기 때문입니다.
    """
    print(greedy(k, coins))

    

def greedy(k, coins):
    coins.sort(reverse=True)

    count = 0

    for coin in coins:
        # print(f'{coin}일 때')
        if k % coin == 0:
            count += (k // coin)
            break
        elif k % coin != 0:
            count += (k // coin)
            k %= coin
        # print(f'{coin}일 때, {count}')

    return count
    

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()