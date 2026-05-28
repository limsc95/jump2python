# 반복문
test_list = ['one', 'two', 'three'] 
for i in test_list:
    print(i)

marks = [90, 25, 67, 45, 80] 

number = 0
for mark in marks:
    number = number + 1 
    if mark < 60: 
        continue
    print(f"{number}번 학생은 합격입니다.")

# 엔드 파라미터 사용 - 줄넘김이 아닌 " " 사용
for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end=" ") 
    print(' ')