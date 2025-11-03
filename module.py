from math import sin, cos, tan
import math as m
print(sin(1))
print(cos(1))
print(tan(1))
print(m.ceil(2.5))
print(m.floor(1.5))

# 함수 데코레이터 : 원래 함수를 인자로 받아, 감싼 새 함수를 리턴한다... 파라미터 주의 
# from functools import wraps
# function → “이 함수 객체 그 자체”
# function() → “이 함수를 지금 실행한 결과(return 값)”
def test(function):
    print('function 함수 시작')
    def wrapper():
        print('wrapper 함수 시작')
        function()
        print('wrapper 함수 끝')

    return wrapper # 이미 return되어 함수 실행 끝
    print('function 함수 끝')

@test
def hello():
    print("hello")

hello()

