def open_account():
  print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):    # 입금
  print("입금이 완료되었습니다. 잔액은 {0}원 입니다".format(balance+money))
  return balance + money

def withdraw(balance, money):    # 출금
  if balance >= money:    # 잔액이 출금보다 많을경우
    print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
    return balance - money
  else:
    print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
    return balance

def withdraw_night(balance, money):    # 저녁 출금
  commission = 100   # 수수료
  return commission, balance - money - commission
  
balance = 50000  # 잔액
balance = deposit(balance, 10000)
# balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 10000)
print("수수료 {0}원이며 잔액은 {1}원 입니다.".format(commission, balance))
