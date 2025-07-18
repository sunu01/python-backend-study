# 클래스변수, 인스턴스 변수 비교

class Dog:
    species = "개"

    def __init__(self, name):
        self.name = name

dog1 = Dog("초코")
dog2 = Dog("밤이")

print(dog1.name)     # 초코
print(dog2.name)     # 밤이
print(dog1.species)  # 개
print(dog2.species)  # 개

Dog.species = "멍멍이"

print(dog1.species)  # 멍멍이
print(dog2.species)  # 멍멍이