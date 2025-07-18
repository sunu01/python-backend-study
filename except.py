# 예외처리
# try:
#     x = int(input("숫자를 입력하세요: "))
#     print(f"입력한 숫자: {x}")
# except ValueError:
#     print("숫자 형식이 올바르지 않습니다!")

#else 구문
# try:
#     x = int(input("숫자를 입력해주세요 : "))
# except ValueError:
#     print("숫자를 입력하세요")
# else:
#     print(f"{x}를 입력하셨습니다.")

#finally 구문
# try:
#     x = int(input("숫자를 입력해주세요 :"))
# except ValueError:
#     print("숫자를 입력하세요")
# finally:
#     print("프로그램 종료")


# try:
#     x = int(input("숫자를 입력해주세요 : "))
#     result = 100/x
# except ValueError:
#     print("숫자를 입력하세요")
# except ZeroDivisionError:
#     print("0으로는 나눌수 없음")
# else:
#     print(f"계산결과 : {result}")
# finally:
#     print("프로그램 종료")

#raise 키워드로 예외 발생
def check_age(age):
    if age<0:
        raise ValueError("나이는 음수 불가")
    else:
        print(f"나이는 {age}입니다")

try:
    check_age(25)
    check_age(-2)
except ValueError as e:
    print(f"에러 발생: {e}")