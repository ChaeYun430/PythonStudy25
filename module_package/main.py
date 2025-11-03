# 현재 파일이 엔트리 포인트인지 확인하는 코드를 통해
# -> import 당하는 모듈에 내부 출력이 실행되지 않는 코드 작성 가능

# pip (Python Package Index) -> 패키지 관리 시스템

# import한 모듈 내부 먼저 출력됨
import test_package.module_a as a
import test_package.module_b as b

print(a.var_a)
print(b.var_b)

if __name__ == '__main__':
    print('module_name(EntryPoint) : ', __name__)
else: 
    print('module_name(Module) : ', __name__)

from test_package import *
print(module_a.var_a)
print(module_b.var_b)