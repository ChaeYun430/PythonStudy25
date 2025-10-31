# 클래스 기반의 객체를 만드는 이유, 생성자와 메서드의 형태에 대해 알아본다. 
class Book:
    # Constructor to initialize book attributes
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Destructor to clean up resources
    def __del__(self):
        print(f"The book '{self.title}' is being removed from the library.")

    # Python에서의 method => member function / instance function
    # 어떤 객체가 가지고 있는 함수(기능)을 명확히 이해할 수 있다. 

    # 객체의 생명주기는?


# isinstance() 함수
book = Book("1984", "George Orwell", 1949)
print(isinstance(book, Book))

