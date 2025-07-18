# #조건문

# age = 20
# if age > 20:
#     print("adult")
# elif age >= 13:
#     print("청소년")
# else:
#     print("어린이")

# #논리연산자
# if age > 18 and age <65:
#     print("일할 수  있습니다")


# score = int(input("점수를 입력하세요 : "))

# if score >= 90:
#     print("A")
# elif score >=80:
#     print("B")
# elif score >=70:
#     print("C")
# elif score >=60:
#     print("D")
# else:
#     print("F")

#함수 기초
# def say_hello():
#     print("안녕하세요")
# say_hello()

# def check_even_odd(number):
#     if number % 2 ==0:
#         print("짝수")
#     else:
#         print("홀수")
# check_even_odd(4)


# def greet(name,age):
#     print(f"안녕하세요, {name}님! 당신은 {age}이군요.")
# greet("순우",26)


# 함수 심화(매개변수, 가변인자, 람다)

def greet(name, age = 26): # age 기본값 20
    print(f"{name}님은 {age}살입니다.")

#가변인자 
#*args: 위치 인자 여러개 받음
# def add_all(*args):
#     return sum(args)
# print(add_all(1,2,34))

#**kwargs : 키워드 인자 여러개 받기(딕셔너리 형태)
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
# print_info(name = "순우", age = 26, heioght = 164)

# 람다 함수

# square = lambda x:x**2
# print(square(5))

# def example(a, b =20, *args, **kwargs):
#     print(f"a ={a},b ={b}")
#     print(f"args = {args}")
#     print(f"kwargs = {kwargs}")

# example(1,2,3,4,5, name = "순우", age = 26)

def greet(name):
    print(f"안녕하세요, {name}님!")

greet("순우")   