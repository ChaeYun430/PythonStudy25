# 클래스 기반의 객체를 만드는 이유, 생성자와 메서드의 형태에 대해 알아본다. 
class Parent:
    # Constructor to initialize book attributes
    def __init__(self, name, birth, job):
        self.name = name
        self.birth = birth
        self.job = job

    # Destructor to clean up resources
    def __del__(self):
        print(f"The parent '{self.name}' is being removed.")

    # Python에서의 method => member function / instance function
    # 어떤 객체가 가지고 있는 함수(기능)을 명확히 이해할 수 있다. 

    # 객체의 생명주기는?

class Child(Parent):
    def __init__(self, name, birth, school):
        super().__init__(name, birth, job=None)
        self.school = school

    def __del__(self):
        print(f"The child '{self.name}' is being removed.")
        super().__del__()

# isinstance() 함수
parent = Parent("parent_name", "1990-01-01", "Engineer")
print(isinstance(parent, Parent))
print(type(parent) == Parent)

child = Child("child_name", "2010-01-01", "Elementary School")
print(isinstance(child, Parent))
print(type(child) == Parent)

