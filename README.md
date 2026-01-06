# 🧠 Baekjoon Algorithm Study (Python)

백준 문제 풀이 기록입니다.  
**목표:** 골드 1 달성!  
**언어:** Python 3  
**코딩테스트 대비용 정리**  

## 목차
[알고리즘별 정리](#-알고리즘별-정리)

[커밋 정리](#커밋-정리)

[태그 활용](#태그-활용-옵션)

[디렉토리 구조](#디렉토리-구조)



## 🧩 알고리즘별 정리

| 알고리즘 | 문제 | 설명 |
|---------|------|------|
| Backtracking | [15649](https://www.acmicpc.net/problem/15649) | 모든 경우를 탐색하며 조건을 만족하는 해를 찾는 방식 |
| Binary Search | [1920](https://www.acmicpc.net/problem/1920) | 정렬된 데이터에서 탐색 범위를 절반씩 줄여 탐색 |
| Brute Force | [2231](https://www.acmicpc.net/problem/2231) | 가능한 모든 경우를 직접 검사 |
| BFS / DFS | [1260](https://www.acmicpc.net/problem/1260), [1012](https://www.acmicpc.net/problem/1012) | 그래프/트리에서 너비·깊이 우선 탐색 |
| DP | [2579](https://www.acmicpc.net/problem/2579), [9095](https://www.acmicpc.net/problem/9095) | 이전 계산 결과를 재사용해 중복 연산 제거 |
| Graph | [2606](https://www.acmicpc.net/problem/2606) | 노드와 간선 관계를 기반으로 문제 해결 |
| Greedy | [11047](https://www.acmicpc.net/problem/11047) | 매 순간 최선의 선택을 하는 알고리즘 |

### DP
#### 0단계. 이게 DP 문제인지부터 판단
아래 키워드가 보이면 DP 의심:

- “최대 / 최소”
- “경우의 수”
- “n번째”
- “~하는 방법”
- “연속”, “누적”
- “최적”

#### 1단계. DP 정의부터 먼저 만든다
"dp[i] = 무엇인가?"

#### 2단계. "i로 오기 직전 상황"을 생각한다
"i번째 상태에 오기 전에, 어디에서 올 수 있지?"

#### 3단계. 점화식 세우기
"dp[i] = (이전 상태들 중에서) + (현재 선택 비용)"

#### 4단계. 초기값 먼저 채운다
`dp[1] = ? dp[2] = ?`

#### 5단계. 계산 방향 결정
```
작은 값 -> 큰 값으로 가야 하나?
큰 값   -> 작은 값으로 가야 하나?
```
#### 6단계. 조건문 구조 체크
```python
dp[i] = 기본값

if 조건1:
    dp[i] = min(dp[i], ...)
if 조건2:
    dp[i] = min(dp[i], ...)
```
`elif` 거의 쓰면 안 됨
왜냐면 **모든 경우를 비교** 해야 하니까



## 정리 팁

```python
# 11047_동전0.py
# https://www.acmicpc.net/problem/11047
# 알고리즘: Greedy
# 핵심 아이디어: 큰 단위 동전부터 사용
```
- 자주 쓰는 코드를 templates/ 폴더에 따로 보관 (예: binary_search_template.py, stack_template.py)


### 커밋 정리
```
Solve: 11047 동전0 (Greedy)
Solve: 1920 수찾기 (Binary Search)
Solve: 2667 단지번호붙이기 (DFS)

```

### 태그 활용 (옵션)

⚙️ 2. 커밋 & 태그 워크플로우

✅ (1) 새 문제 푼 뒤 커밋
```bash
git add 1920_수_찾기.py
git commit -m "solve: BOJ 1920 수 찾기 (binary search / set)"

```
✅ (2) 태그 붙이기
```bash
git tag -a boj/1920 -m "BOJ 1920 수 찾기"
```

✅ (3) GitHub에 태그 푸시
```bash
git push origin main
git push origin boj/1920
```


### 디렉토리 구조
```
baekjoon/
│
├── README.md                # 공부 기록 or 회고 정리
├── requirements.txt         # (선택) 자주 쓰는 라이브러리 관리용
│
├── solved_class/            # 백준 Class별 분류 (권장)
│   ├── class1/
│   │   ├── 1000_A+B.py
│   │   ├── 2557_HelloWorld.py
│   │   └── README.md
│   ├── class2/
│   │   ├── 1920_수찾기.py
│   │   ├── 2164_카드2.py
│   │   └── README.md
│   └── ...
│
├── by_algorithm/            # 알고리즘 유형별 분류 (선택)
│   ├── dp/
│   │   ├── 1463_1로만들기.py
│   │   ├── 2579_계단오르기.py
│   │   └── README.md
│   ├── graph/
│   │   ├── 1260_DFS와BFS.py
│   │   ├── 2606_바이러스.py
│   │   └── README.md
│   └── ...
│
├── templates/               # 자주 쓰는 코드 스니펫
│   ├── bfs_template.py
│   ├── dfs_template.py
│   ├── dijkstra_template.py
│   └── ...
│
└── utils/                   # 공통 함수/입출력 관리
    ├── fast_io.py
    ├── math_utils.py
    └── ...


```