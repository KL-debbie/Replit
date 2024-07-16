import random

num = random.randint(0, 99)
print(num)
print(str(num).zfill(5))
#-----------------------------------------------
class Account:

  account_count = 0    # 계좌가 만들어질때마다 생성자 호출

  def __init__(self, name, balance):
    self.deposit_count = 0 # 입금 횟수
    self.deposit_log = []
    self.withdraw_log = []
    
    self.name = name
    self.balance = balance
    self.bank = "SC은행"
    #계좌번호 생성
    num1 = random.randint(0, 999)  # 3자리
    num2 = random.randint(0, 99)  # 2자리
    num3 = random.randint(0, 999999)  # 6자리

    num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
    num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
    num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
    self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001

    Account.account_count += 1    # 계좌가 만들어질때마다 생성되므로 1씩 증가

  def get_account_num(cls):
    print(cls.account_count)      # Account.account_count 생성된 계좌의 갯수 출력

  def deposit(self, amount):      # 입금 메서드, amount 입금액
    if amount >= 1:    # 1원 이상 입금 가능
      self.deposit_log.append(amount)    # 입금할때마다 리스트에 저장
      self.balance += amount

      # 이자 지급
      self.deposit_count += 1
      if self.deposit_count % 5 == 0:    # 입급 횟수가 5회가 될 때
        # 이자 지금
        self.balance = self.balance * 1.01

  def withdraw(self, amount):      # 출금 메서드
    if self.balance > amount: 
      self.withdraw_log.append(amount)    # 출금 매역
      self.balance -= amount

  def display_info(self):        # 정보 출력
    print('bank :', self.bank)
    print('name :', self.name)
    print('Account :', self.account_number)
    print('balance :', f"{self.balance:,}")    # 3자리마다 , 출력하기

  def withdraw_history(self):    # 출금
    for amount in self.withdraw_log:
      print(amount)
      
  def deposit_history(self):    # 입금
    for amount in self.deposit_log:
      print(amount)
# 계좌 객체 개수
'''
kim = Account("김민수", 100)
print(Account.account_count)
lee = Account("이민수", 100)
print(Account.account_count)
'''

# 계좌 생성
kim = Account("김민수", 100)
print(kim.name)
print(kim.balance)
print(kim.bank)
print(kim.account_number)
print(Account.account_count)


# 입금 출금
kimm = Account('leee', 157)
print(kimm.name)
print(kimm.balance)
kimm.deposit(100)
kimm.withdraw(90)
print(kimm.balance)
print(Account.account_count)

# Account 정보 출력
pyy = Account('py', 100000)
pyy.display_info()

# 이자 지급
p = Account("py", 10000)
p.deposit(100000)
p.deposit(100000)
p.deposit(100000)
p.deposit(33300)
p.deposit(33300)
print(p.balance)

# 인스턴스 리스트 저장
data = []
k = Account('KIM', 100000)
l = Account('LEE', 1000000000000)
p = Account('PARK', 1000000000)

data.append(k)
data.append(l)
data.append(p)

#  1000000만원 이상인 고객 정보 출력
for c in data:
  if c.balance >= 1000000:
    c.display_info()

# 입금 출금 내역
c = Account("CHO", 300)
c.deposit(300)
c.deposit(300)
c.deposit(300)
c.deposit(300)
c.deposit_history()

c.withdraw(400)
c.withdraw(400)
c.withdraw_history()