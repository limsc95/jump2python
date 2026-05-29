# 내장 함수

# abs 절대값 반환
abs(-3)

# all 모든게 있는 경우 참
words = ["apple", "ant", "arrow"]
print(all(w.startswith("a") for w in words))

# any 하나라도 맞다면 참
list1 = [1,2,3]
print(any(x > 2 for x in list1))

# chr 유니코드 값 <-> ord 
print(chr(97)) # a
print(chr(44032)) # 가
print(ord('a')) # a
print(ord('가')) # 가

# divmod 몫과 나머지
x, y = divmod(12,5)
print(x, y)

# enumerate 열거
enumerateList = ["zero", "one", "two", "three"]
for i, j in enumerate(enumerateList):
    print(i , j)

# filter
def positive(x): 
    result = [] 
    for i in x: 
        if i > 0: 
            result.append(i) 
    return result

print(positive([1,-3,2,0,-5,6]))

# int() 숫자 변환
int("3") # 3
int(3.5) # 3
int('11',2) # 2진수 변환 3
int('1A',16) # 16진수 변환 26

# len 길이 반환
print(len("python"))
print(len([1,2,3]))

#map
def two_times(numList):
    result = []
    for num in numList:
        result.append(num *2)
    return result

result = two_times([1,2,3,4])
print(result)

# max, min, sum 최대, 최소, 합
nums = [3, 1, 4, 1, 5, 9]
print(max(nums))  # 9
print(min(nums))  # 1
print(sum(nums))  # 23

# pow 제곱
print(pow(2,10))

# range 범위 값 ([start], stop, [step])
print(list(range(5)))
print(list(range(1, 10, 2)))

# zip 동일한 개수로 이루어진 데이터를 묶어서 반환
print(list(zip("012",["zero", "one", "two"])))