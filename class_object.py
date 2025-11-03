# 클래스 기반의 객체를 만드는 이유, 생성자와 메서드의 형태에 대해 알아본다. 
class Parent:
    # Constructor to initialize book attributes
    def __init__(self, name, birth, job):
        self.name = name
        self.birth = birth
        self.job = job

    # Destructor to clean up resources
    # 객체가 생성되고 나서 더 이상 참조되지 않으면, garbage collector가 이를 감지하여 메모리에서 해제한다.
    def __del__(self):
        print(f"The parent '{self.name}' is being removed.")

    # Python에서의 method => member function / instance function
    # 어떤 객체가 가지고 있는 함수(기능)을 명확히 이해할 수 있다. 


class Child(Parent):
    def __init__(self, name, birth, school):
        super().__init__(name, birth, job=None)
        self.school = school

    def __del__(self):
        print(f"The child '{self.name}' is being removed.")
        super().__del__()

# isinstance() 함수 (상속 관계까지 확인)
parent = Parent("parent_name", "1990-01-01", "Engineer")
print(isinstance(parent, Parent))
print(type(parent) == Parent)

child = Child("child_name", "2010-01-01", "Elementary School")
print(isinstance(parent, Child))
print(isinstance(child, Parent))
print(type(child) == Parent)

# 노트북 작성 코드 백업 바람

# Dunder method를 활용한 (TypeError 등) 예외 처리
# 타입이 다른 두 대상을 활용하는 기능을 구현할 때 메서드 내에 비교 대상을 한정하고 조건에 따라 구현한다.

# 객체간의 속성 공유 여부 (static variable vs instance variable)
class Sample:
    array = []  # 클래스 변수 (모든 인스턴스가 공유)

    def __init__(self, value):
        self.value = value  # 인스턴스 변수 (각 인스턴스가 개별적으로 가짐)
        Sample.array.append(value)
    
    def __str__(self):
        return "{}, {}".format(self.value, Sample.array)
    
    @classmethod # decorator
    def print(cls):
        for i in range(len(cls.array)):
            print(i, cls.array[i])

Sample(1)
Sample(2)
Sample(3)
Sample(4)
Sample(5)
Sample.print()

# 변수에 대한 접근 제어 (private, protected, public)
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self.__radius = value
    
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    
circle = Circle(5)
# print("Radius:", circle.__radius)
# AttributeError: 'Circle' object has no attribute '__radius'
print("Radius:", circle.get_radius())
circle.set_radius(10)
print("Updated Radius:", circle.get_radius())

class CustomException(Exception):

    def __init__(self, value):
        Exception.__init__(self)
        self.value = value
    
    def __str__(self):
        return "Dunder Method __str__"

    def print(self):
        print("오류출력")

try:
    raise CustomException("call print()")
except CustomException as e:
    e.print()

raise CustomException("call str()")
