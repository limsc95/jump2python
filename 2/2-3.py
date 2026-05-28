#리스트 자료
a = [1, 4, 3, 2, 5]

# [2] 삭제
del a[2]
print(a)

# 6 추가
a.append(6)
print(a)

# 정렬
a.sort()
print(a)

a.reverse()
print(a)

# 인덱스 반환
print(a.index(1))

# 삽입
a.insert(1, 7)
print(a)

# 리스트 요소 삭제
a.remove(5)
print(a)

# 꺼내기
print(a.pop(0))