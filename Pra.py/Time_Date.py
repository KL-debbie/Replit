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

cal = calendar.month(year, month)
print(cal)

print('------------------------')
