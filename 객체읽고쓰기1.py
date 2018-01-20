import pickle # 객체를 직렬화 해주는 클래스

class MyClass:
    def __init__(self, name="", phone="", address=""):
        self.name = name
        self.phone = phone
        self.address = address

    def output(self):
        print("이름:", self.name)
        print("전화:", self.phone)
        print("주소:", self.address)

myList = [
    MyClass("홍길동", "010-9999-0000", "강남구"),
    MyClass("임꺽정", "010-9999-1111", "서초구"),
    MyClass("장길산", "010-9999-2222", "관악구"),
    MyClass("홍결래", "010-9999-3333", "금천구"),
    MyClass("이순신", "010-9999-4444", "용산구"),
]

