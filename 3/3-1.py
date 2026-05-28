# if문
money = 3000
if money > 2000:
    print("택시 이용")
else:
    print("도보 이용")

grade = 'A'
match grade:
    case 'A':
        print('탁월')
    case 'B':
        print('우수')
    case 'C':
        print('보통')
    case _:
        print("노력 필요")
    