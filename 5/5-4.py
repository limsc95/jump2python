# 예외 처리
try:
    print("나누기 전")
    4 / 0
    print("나누기 후")
except ZeroDivisionError:
    print("오류가 발생했습니다.")
finally:
    print("finally 실행!")