# 2609_최대공약수와 최소공배수.py
# https://www.acmicpc.net/problem/2609
# 알고리즘: 
# 핵심 아이디어: 

import sys
import math

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main(): 

    a, b = map(int, input().split())

    print(math.gcd(a, b))
    print(a * b // math.gcd(a, b))
    

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()