# 파일 읽고 쓰기
# 쓰기
# f = open("C:\\sources\\Coding-Test\\python\\4\\text.txt", 'w', encoding="utf-8")
# for i in range(1, 11):
#     data = f"{i}번째 줄입니다.\n"
#     f.write(data)
# f.close()

# 읽기
# f = open("C:\\sources\\Coding-Test\\python\\4\\text.txt", 'r', encoding="utf-8")

# 한줄 읽기
# line = f.readline()
# print(line)

# 모든 줄 읽기
# lines = f.readlines()
# for line in lines:
#     line = line.strip()
#     print(line, end=" ")

# 파일 객체 읽기
# for line in f:
#     print(line)
# f.close

# 내용 추가
# w 의 경우 여는 순간 내용 삭제로 인해 a로 추가
f = open("C:\\sources\\Coding-Test\\python\\4\\text.txt", 'a', encoding="utf-8")

for i in range(11,20):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)

f.close