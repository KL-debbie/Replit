'''사용자로부터 입력 받기'''
user = input('입력 : ')
print(user *2 )

user = input('숫자 입력 : ')
print(10 + int(user) )

user = input('숫자 입력 : ')
if int(user) % 2 == 0:
  print('짝수')
else:
  print('홀수')

user = input('숫자 입력 : ')
num = int(user) - 20
if num > 255:
  print(255)
elif num  < 0:
  print(0)
else:
  print(num)

fruit = ["사과", "포도", "홍시"]
sel = input('좋아하는 과일???')
if sel in fruit:
  print('corrrr')
else:
  print('noooo')

warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
invest = input('종목명 ? ')
if invest in warn_investment_list:
  print('Warn')
else:
  print('okkk')

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input('좋아하는 계절 :')
if user in fruit:
  print('정답')
else:
  print('오답')

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input('좋아하는 과일 :')
if user in fruit.values():
  print('정답')
else:
  print('오답')

