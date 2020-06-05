# 5월 3째주 시작

### jd
-

### hc

#### 11866

- https://www.acmicpc.net/problem/11866

|메모리|시간|누구|
|--|--|--|
|<del>31848KB|<del>112ms|<del>hc|
|29380KB|60ms|gus|

- Improvement
  - gus
    - Queue 안쓰고 규칙을 찾아서 List로 구현
    - 시간복잡도 O(N)
- Lessons Learned
    1. index 계산할 때, 현재 배열을 초과하여 생각하면 편함
        ```
        a = [1, 2, 3]
        5번째 값을 구한다면?
        a[5 - len(a)]
        ```
    1. index를 생각할 때, 1부터 세고 싶으면 실질적인 함수를 콜 할때 `pop(i-1)` 처럼 1을 빼주면 생각하기 편함

### gus
- https://www.acmicpc.net/problem/13699

|메모리|시간|누구|
|--|--|--|
|29380KB|64ms|gus|

- Lessons Learned
    1. 해쉬 함수로는 dict 구조체를 쓰면 된다.
        ```
        my_hash = {} // 선언
        my_hash[1] = 10 // key: int, value: int, 입력
        my_hash[1] // 출력
        ```
    1. recursive 함수는 따로 처리할건 없다.
        ```
        def rec():
            return rec()
        ```
    1. for loop
        ```
        for i in range(5) // 0, 1, 2, 3, 4
        ```
    1. global 변수는 write 할 경우에만 함수안에 global keyword 사용
        ```
        x = 0
        def read_x():
            print(x) 
        def write_x():
            global x
            x = 1
        ```
    

### jack

- https://www.acmicpc.net/problem/1261
  
|메모리|시간|누구|
|--|--|--|
|31824KB|232ms|jack|
