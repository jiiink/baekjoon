# 1920_수 찾기.py
# https://www.acmicpc.net/problem/1920
# 알고리즘: binary_search
# 핵심 아이디어: 큰 리스트에서 탐색 or 효율적인 자료구조

import sys
input = sys.stdin.readline

def main():
    n1 = int(input().strip())
    arr1 = list(map(int, input().split()))

    n2 = int(input().strip())
    arr2 = list(map(int, input().split()))

    arr1.sort() # 이진탐색을 위한 정렬

    for num in arr2:
        print(binary_search(arr1, num))    

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    
    while (left <= right):
        mid = (left + right) // 2

        if (target == arr[mid]):
            return 1
        elif (target < arr[mid]):
            right = mid - 1
        else:
            left = mid + 1

    return 0

def main2():
    n1 = map(int, input().strip())
    arr1 = list(map(int, input().split()))
    n2 = map(int, input().strip())
    arr2 = list(map(int, input().split()))

    arr1 = set(arr1)
    for target in arr2:
        print(1 if target in arr1 else 0)

if __name__ == "__main__":
    # 테스트 입력이 있을 경우 아래 주석 해제
    # sys.stdin = open("input.txt", "r")
    # main() # binary_search
    main2() # set()