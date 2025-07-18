# 변수와 자료형
# name = "soonwoo"
# age = 26
# height = 165.0
# is_student = True
# print(name, age, height, is_student)
# print(f"이름 : {name}, 나이 : {age}, 키 : {height}, 학생여부 : {is_student}")

#조건문
# score = int(input("점수를 입력해주세요 : "))
# if score >= 90:
#     print("A학점")
# elif score >= 80:
#     print("B학점")
# else:
#     print("C학점 이하")

#반복문
# for i in range(5):
#     print(f"{i}번째 반복")

# count = 0
# while count < 3:
#     print(f"while 반복 : {count}")
#     count += 1

# # 함수
# def greet(name):
#     return(f"반갑습니다 {name}님!")
# print(greet("soonwoo"))

# 예외처리
try:
    num = int(input("숫자를 입력하세요 : "))
    print(f"입력한 숫자의 2배: {num *2}")
except ValueError:
    print("숫자만 입력하세요요")