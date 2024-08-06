# 생일이 얼마나 남았는지 계산
import datetime

month = int(input("태어난 달 : "))
day = int(input("태어난 일 : "))

# 현재 연도를 사용하여 생일 날짜를 생성합니다.
current_year = datetime.datetime.now().year
birthday = datetime.datetime(current_year, month, day)
today = datetime.datetime.now()

# 만약 생일이 이미 지났다면, 다음 해의 생일을 계산합니다.
if birthday < today:
    birthday = datetime.datetime(current_year + 1, month, day)

# 생일까지 남은 일수를 계산합니다.
untilbirth = birthday - today

print("생일은 ", untilbirth.days, "일 남았습니다.")

print('----------------------------------------------')
# tip 계산
star = int(input('별점 입력(1-5) : '))
bill = float(input('음식 값 입력 : '))
people = int(input('인원 수 입력 : '))

tipPercent = 0

if star == 1:
  tipPercent = 5
elif star == 2:
  tipPercent = 10
elif star == 3:
  tipPercent = 15
elif star == 4:
  tipPercent = 20
else:
  tipPercent = 25

tip = bill * tipPercent/ 100
total = bill + tip
person = total/people
print(round(person,2))

print('----------------------------------------------')

