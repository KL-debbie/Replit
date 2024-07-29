# 타이머
import time
dur = int(input('타이머 설정 시간(초) 입력하세요 : '))
print(f"{dur}초 타이머 시작")

time.sleep(dur)
print('타이머 종료')

print('------------------------')

# 달력
import calendar

year = int(input("년도 입력 : "))
month = int(input("월 입력 : "))

cal = calendar.month(year,month)
print(cal)

print('------------------------')
# 팩토리얼

def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n-1)

n = int(input("숫자 입력 : "))
print(f"{n}의 팩토리얼은 {factorial(n)}")

print('------------------------')

