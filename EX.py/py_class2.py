import random
from sre_constants import AT_LOC_NON_BOUNDARY

class Account:

  account_count = 0
  
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
    self.bank = "SC은행"
    num1 = random.randint(0, 999)
    num2 = random.randint(0, 99)
    num3 = random.randint(0, 999999)

    num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
    num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
    num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
    self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
    
    Account.account_count += 1

  def get_account_num(cls):
    print(cls.account_count)      # Account.account_count
  
  def deposit(self, amount):      # 입금 메서드
    if amount >= 1:
      self.balance += amount

  def withdraw(self, amount):
    if self.balance > amount:
      self.balance -= amount

  def display_info(self):
    print('bank :', self.bank)
    print('name :', self.name)
    print('Account :', self.account_number)
    print('balance :', f"{self.balance:,}")

# 계좌 객체 갯수
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

# 입금 출금
kimm = Account('leee', 157)
print(kimm.name)
print(kimm.balance)
kimm.deposit(100)
kimm.withdraw(90)
print(kimm.balance)

pyy = Account('py', 100000)
pyy.display_info()
#------------------------------------------
class car:
  def __init__(self,wheel,price):
    self.wheel = wheel
    self.price = price

class 자동차(car):
  def __init__(self, wheel, price):
      super().__init__(wheel, price)

  def info(self):
      print("wheel ", self.wheel)
      print("price ", self.price)


car1= car(4, 1000)
 