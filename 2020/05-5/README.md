# 5월 5째주 시작

### hc

- https://www.acmicpc.net/problem/1920

|메모리|시간|누구|Comment|
|--|--|--|--|
|<del>225788KB|<del>7876ms|<del>Hyeongcheol-An||
|43468KB|720ms|Jack|어떻게 그렇게 짰는지 잘 모르겠음|

- 이분탐색 구현
  - 파이썬 속도를 느낄 수 있었음  


### gus

- https://www.acmicpc.net/problem/1532

|메모리|시간|누구|
|--|--|--|
|29380KB|160ms|gus|

- Lessons Learned
  - 시뮬레이션 카테고리
    1. 문제를 읽으면 흡사 BFS 로 풀 수 있을 것만 같다
    2. 시뮬레이션은 주어신 상황에서, 선택에 대한 경우의 수가 발생하지 않는다.
    3. 그 부분을 파악하는 것이 문제의 핵심이다.
  - 전역 변수
    - `if __name__ == "__main__":` 과 같은 레벨에 선언된 변수
    - `def A()` 함수 안에서 사용하려면, write 하기 위해선 global 태그 표시
    - `__main__` 영역 안에서는 그냥 사용해도 된다
  

### jack

- https://www.acmicpc.net/problem/2805

|메모리|시간|누구|
|--|--|--|
|146860KB|4904ms|Jack|

- Lessons Learned
  - 이진탐색 카테고리
    - 카테고리를 몰랐다면 과연 이진탐색으로 풀었을까 하는 생각이 든다.
    - 익숙해지기 위해 더 많은 문제들을 풀어봐야 할 것이다.
  - // 연산자
    - int 형변환 대신 사용하면 좀 더 빨라진다
