# 문제번호_제목.py
# url
# 알고리즘: 
# 핵심 아이디어: 

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main(): 
    # 입력 받기 예시 -----------------------------
    # 한 줄에 정수 하나
    k = int(input().strip())

    money = []
 
    for _ in range(k):
        num = int(input().strip())
        if num == 0:
            money.pop()
        else:
            money.append(num)

    print(sum(money))
    
if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()