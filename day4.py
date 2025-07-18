# 파일 열기 
# f = open("파일이름.txt", "모드")

# 파일 쓰기
f = open("hello.txt", "w")
f.write("안녕하세요\n")
f.write("파이썬을 배워봅시다\n")
f.close

#파일 읽기(read, readline, readlines)
# f = open("hello.txt", "r")
# print(f.read())
# f.close

# f = open("hello.txt", "r")
# print(f.readline()) # 한줄만 읽기
# f.close

# f = open("hello.txt", "r")
# lines = f.readlines()
# print(lines)
# for line in lines:
#     print(line.strip()) # line.strip()은 문자열에서 앞뒤 공백(특히 줄바꿈 문자 \n)을 제거합니다.
#                         #"안녕하세요\n"라는 문자열이 strip() 메서드를 거치면 "안녕하세요"가 됩니다.
# f.close

#with 문을 사용한 자동 닫기
# with open("hello.txt", "r") as f:
#     data = f.read()
#     print (data)

# 텍스트 파일 쓰기
with open("example.txt","w")as file:
    file.write("안녕하세요. 파이썬 파일 입출력 실습입니다.")

# 텍스트 파일 읽기
with open("example.txt","r") as file:
    content = file.read()
    print(content)

# 여러 줄 쓰기
lines = ["첫번째 줄\n","두 번째 줄\n","세번째 줄\n"]
with open("lines.txt", "w") as file:
    file.writelines(lines)

# 한줄씩 읽기 한줄만 읽기
with open("lines.txt","r") as file:
    print(file.readline())

#모든 줄을 리스트로 읽기
with open("lines.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())