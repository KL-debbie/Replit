def print_coin():
  print('비트코인')

print_coin() #함수 호출

''' 100번 호출
for i in range(100):
  print_coin()
'''

def print_coins():
  for i in range(100):
      print("비트코인")

'''
함수 호출
def message() :
  print("A")
  print("B")

message()
print("C")
message()
----------------------------
def message1():
  print("A")

def message2():
  print("B")
  message1()

message2()
----------------------------
def message1():
  print("A")

def message2():
  print("B")

def message3():
  for i in range (3) : # 0,1,2
      message2()
      print("C")
  message1()

message3()
'''

# 함수 선언 및 호출
def print_with_smile(str):
  print(str + ':D')

print_with_smile('hello~')

def print_upper_price(price):
  print(price * 1.3)

print_upper_price(300)

def print_sum(a, b):
  print(a + b)

def print_arithmetic_operation(a, b):
  print(a , '+', b, '=', a+b)
  print(a , '-', b, '=', a-b)
  print(a , '/', b, '=', a/b)
  print(a , '*', b, '=', a*b)

print_arithmetic_operation(3,4)

# 최대 최소 구하기
def print_max(a, b, c):
  if a > b and a > c:
   print(a)
  elif b > a and b > c:
    print(b)
  else:
    print(c)

print_max(10,34,33)

