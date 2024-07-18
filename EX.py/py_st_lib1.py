# date 함수
# datetime.date 연,월,일 날짜표현
import datetime
day1 = datetime.date(2024,7,17)
day2 = datetime.date(2024,6,1)
dif = day1 - day2
print(dif.days)

# weekday() 요일 반환 0-월요일, ---, 6-일요일
day = datetime.date(2024,7,18)
print(day.weekday())

# isoweekday() 요일반환 1-월요일, ---, 7-일요일
day = datetime.date(2024,7,18)
print(day.isoweekday())

#-----------------------------------------------------------------
# time 함수
# time.time 1970년 1월 1일 0시 0분 0초 기준으로 지난 시간을 초 단위로 리턴
import time
print(time.time())

# localtime() 리턴한 실수값을 연,월,일,시,분,초,..의 형태로 바꿔주는 함수
print(time.localtime())

# asctime() 리턴된 튜플 형태의 값을 인수로 받아 날짜와 시간을 알아보기 쉬운 형태로 리턴하는 함수, struct_time 객체를 입력 받음
print(time.asctime())

# ctime() asctime()과 비슷, 현재 시간만 리턴한다는 점 주의
print(time.ctime())

# strtime() 시간에 관계된 것을 세밀하게 표현하는 포맷 코드 제공
# 코드 확인

# sleep() 일정한 시간 간격을 두고 루프 실행 가능

#-----------------------------------------------------------------
# math 함수
import math

# 최대공약수 구하기 gcd()
gcd = math.gcd(60,100,80)
print(gcd)

# 최소공배수 구하기 lcm()
lcm = math.lcm(60,100,80)
print(lcm)

#-----------------------------------------------------------------
# random 함수
import random

# 0.0 ~ 1.0 사이의 실수 중 난수 값 리턴
rnd = random.random()
print(rnd)

# 1 ~ 10 사이의 정수 중 난수 값 리턴
rnd1 = random.randint(1,10)
print(rnd1)

#-----------------------------------------------------------------
# itertools 함수
import itertools

# itertools.zip_longest(iterables, fillvalue = None)
# 같은 개수의 자료형을 묶는 zip 함수와 같은 동작
# iterables 길이가 다르면 긴 객체의 길이에 맞춰 fillvalue에 설정한 값을 짧은 객체에 채울 수 있음
# fillvalue에 값을 지정하면 None 대신 값을 채울 수 있음
students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초컬릿', '젤리']
# 새우깡으로 채우기
result = itertools.zip_longest(students, snacks, fillvalue='새우깡')
print(list(result))

# permutation(iterable, r) 순열 구하기
# 반복 가능 객체 중에서 r개를 선택한 순열을 이터레이터로 리턴하는 함수
per = list(itertools.permutations(['1', '2', '3'], 2))
print(per)

# combinations(iterable, r)
# 반복 가능 객체 중에서 r개를 선택한 조합을 이터레이터로 리턴하는 함수

# 1~45의 숫자 중에서 6개를 뽑는 경우의 수
it = itertools.combinations(range(1, 46), 6)
it = len(list(it))  # 이터레이터 개수 세기
print(it)

#-----------------------------------------------------------------
