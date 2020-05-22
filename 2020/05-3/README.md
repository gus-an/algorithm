# 5월 3째주 시작

### jd
-

### hc

#### 11866

- https://www.acmicpc.net/problem/11866

|메모리|시간|누구|
|--|--|--|
|31848KB|112ms|hc|

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
