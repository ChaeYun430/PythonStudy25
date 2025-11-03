# 가변 매개변수 뒤에는 일반 매개변수가 올 수 없다. 
# 가변 매개변수는 하나만 사용할 수 있다. 
# 기본 매개변수 뒤에는 일반 매개변수가 올 수 없다.      
def print_n_times(n, *values):
    for i in range(n):
        for value in values: # 리스트처럼 활용
            print(value, end = ' ')
        print()
print_n_times(3, '가', '나', '다', '라')

# (기본+가변) 무의미 
# (가변+기본) 가변 매개변수가 우선되고 기본값으로 그대로 초기화된다.
# 키워드 매개변수 :  매개변수의 이름을 지정하여 입력한다.(매개변수 순서 변경가능)
def print_n_times(*values, n=5):
    for i in range(n):
        for value in values: # 리스트처럼 활용
            print(value, end = ' ')
        print()
print_n_times('A', 'B', 'C', 4)
print_n_times('A', 'B', 'C', n=4)
print_n_times(1, 2, 'A', 'B', 'C', n=6)
print_n_times(3, '가', '나', '다', '라') # 함수 오버라이딩에 대해 궁금;;

## 함수 내의 return
# 함수를 실행했던 위치로 돌아가라
# 함수를 여기서 끝내라
# 아무것도 return 하지 않으면 None이 할당된다.

## 재귀함수
def factorial1(n):
    outp