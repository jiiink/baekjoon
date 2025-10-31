# 7568_덩치.py
# https://www.acmicpc.net/problem/7568
# 알고리즘: 
# 핵심 아이디어: 비교 기준

import sys

# 빠른 입력 (input() 대신 사용)
input = sys.stdin.readline

def main():
    people = []

    n = int(input().strip())

    for _ in range(n):
        person = list(map(int, input().split()))
        # print(person)
        person.append(1)
        people.append(person)

    # print(people)

    compare(people)


    # print("---------------")
    for person in people:
        print(person[2], end=" ")
    

def compare(people):
    # 여기에 풀이 로직 작성
    for i in range(len(people)):
        for person in people:
            if (people[i][0] < person[0] and people[i][1] < person[1]):
                people[i][2] += 1

    return

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    main()