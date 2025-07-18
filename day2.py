#리스트 기초 실습
# fruit = ["banna", "apple", "grape"]
# print(fruit)
# #추가
# fruit.append("cherry")
# #삭제
# fruit.remove("grape")
# #정렬
# fruit.sort()
# print(fruit)

# 딕셔너리 기초 실습
# person = {"name" : "soonwoo", "age":"26"}
# print(person)

# #값가져오기
# print(person["name"])

# #값 변경
# person["age"] = 27

# #키 값 추가
# person["job"] = "developer"

# print(person)

# numbers = [1,2,3,4,5]
# squares = [x**2 for x in numbers]
# print(squares)

# numbers =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# number = [x**2 for x in numbers if x % 2 == 0]
# print(number)\

def greet(name="익명", msg = "안녕하세요"):
    return(f"{msg},{name}님")
print(greet())
print(greet("soonwoo"))
print(greet(msg = "환영합니다다"))