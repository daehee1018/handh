'''
#문제 1 
#split() → 공백 기준으로 문자열을 나눔
num1, num2 = input().split()
print(int(num1)+int(num2))

#문제 2 
num1, num2 = map(int, input().split())
print (f'몫 : {int(num1/num2)}, 나머지 :{num1%num2}')

#문제 3 
print(2**10)

#문제 4
number = int(input())
minutes = int(number/60) # == number//60   / = 나누기 (실수) // = 정수 나누기
seconds = int(number%60)
print(f'{minutes}분 {seconds}초')

#문제 5
number = int(input())

a = int(number/500)
b = int(number%500/100)
c = int((number%500)%100/50)
d = int((number%500)%100%50/10)


print(f'500원 {a}개, 100원 {b}개, 50원 {c}개, 10원 {d}개')
#문제 6(BMI = 체중(kg) / 신장(m)²)
BMI가 18.5 이하면 저체중
BMI가 18.5 ~ 22.9 사이면 정상
BMI가 23.0 ~ 24.9 사이면 과체중
BMI가 25.0 이상부터는 비만

height = float(input('키(m) : '))
weight = float(input('몸무게(kg) : '))
bmi = weight/(height**2)
print(f'BMI : {bmi:.01f}')
# 소수점 관련 링크 https://blockdmask.tistory.com/534
'''

'''
2. 문자열 자료형
#문제 1
string = "Jump to Python"
print(len(string))
#문제 2
string = "Python 
print(string[:6])
#문제 3
string = "Python"
print(string[::-1])

#문제 4
s = 'beautiful'
s1 = s.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
print(s1)

#문제 5
s= 'python is fun'
print(len(s.split()))

#문제 6
s = "python programming"
print(s.replace(" ", "_"))  

# 3 
#문제 1 
lst = [10, 20, 30, 40, 50]
print(lst[2]) 

#문제 2
lst = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print([lst[0], lst[2], lst[4]])  

# 문제 3 
lst = [5, 10, 15, 20, 25]
print(sum(lst)) 

# 문제 4
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(lst.index(1))  

# 문제 5
lst = ['apple', 'banana', 'apple', 'orange', 'apple']
print(lst.count('apple'))  

# 문제 6 
lst = [10, 20, 30, 40, 50]
lst[0], lst[-1] = lst[-1], lst[0]
# 가운데 요소 제거
del lst[len(lst) // 2]
print(lst) 

'''
'''
#1
birth_year = int(input())  # 출생 연도 입력
name = input()  # 이름 입력
weight = float(input())  # 몸무게 입력

current_year = 2025  # 현재 연도
age = current_year+1 - birth_year  # 과거 한국식 나이 계산

print(f'이름: {name}, 출생 연도: {birth_year}년, 나이: {age}세, 몸무게: {weight}kg')

#2
index = int(input())  # 인덱스 번호 입력
word = input()  # 단어 입력
repeat_count = int(input())  # 반복 횟수 입력

selected_char = word[index]  # 인덱스 위치의 문자 선택
repeated_result = selected_char * repeat_count  # 해당 문자 반복

print(f'선택된 문자: {selected_char}, 반복 결과: {repeated_result}')


#3
category = input()  # 상품 카테고리 입력
brand = input()  # 브랜드명 입력
year = int(input())  # 제품 출시 연도 입력

# 1. 대소문자 구분 없이 모음 제거
filtered_category = category.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "") \
                             .replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "")


# 2. 브랜드명에서 첫 두 글자 추출
brand_code = brand[:2]

# 3. 연도 계산 (앞 두 자리 + 뒤 두 자리)
year_sum = (year // 100) + (year % 100)  # 2023 → (20) + (23) = 43

# 4. 최종 상품 코드 생성
product_code = filtered_category[:5]  + brand_code + str(year_sum)

print(f'생성된 상품 코드: {product_code}')

'''












