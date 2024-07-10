'''사용자로부터 입력 받기'''
user = input('입력 : ')
if user.islower():
  print(user.upper())
else:
  print(user.lower())

'''점수'''
user = int(input('점수 입력 : '))
if 81 <= user and user <= 100:
  print('grade is A')
elif 61 <= user and user <= 80:
  print('grade is B')
elif 41 <= user and user <= 60:
  print('grade is C')
elif 21 <= user and user <= 40:
  print('grade is D')
else:
  print('grade is E')

'''최댓값/최솟값'''
user1 = int(input('number1 : '))
user2 = int(input('number2 : '))
user3 = int(input('number3 : '))

if user1 > user2 and user1 > user3:
  print(user1)
elif user2 > user1 and user2 > user3:
  print(user2)
else:
  print(user3)

'''통신사'''
tel = input('번호 입력 : ')
num = tel.split('-')[0]
if num == '011':
  com = 'SKT'
elif num == '016':
  com = 'KT'
elif num == '019':
  com = 'LGU'
else:
  com = 'None'
print(f"당신은 {com} 사용자")

'''우편번호'''
add_num = input('우편 번호 : ')
addr = add_num[:3]
if addr in ['010','012','013']:
  print('강북구')
elif addr in ['014','015','016']:
  print('도봉구')
else:
  print('노원구')

'''주민번호'''
user = input('주민번호 : ')
users = user.split('-')[1]
if users[0] == '1' or users[0] == '3':
  print('남자')
else:
  print('여자')

'''주민번호 뒷자리 두,세번째 코드'''
back = user.split('-')[1]
if 0 <= int(back[1:3]) <=8:
  print('seoul')
else:
  print('busan')

'''주민번호 유효성 체크'''
num = input("주민등록번호: ")
계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
        int(num[11])* 4 + int(num[12]) * 5
계산2 = 11 - (계산1 % 11)
계산3 = str(계산2)

if num[-1] == 계산3[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

