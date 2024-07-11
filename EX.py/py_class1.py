class Human:
  def __init__(self,name,age,gender):
    self.name = name
    self.age = age
    self.gender = gender

  def who(self):
    print('이름 :', self.name, '나이 :', self.age, '성별 :', self.gender)

  def selfInfo(self,name,age,gender):
    self.name = name
    self.age = age
    self.gender = gender

  def __del__(self):
    print("nooooooooooo")
    
areum = Human("모름", 0, "모름")
areum.who()
areum = Human("아름", 25, "여자")
del areum
#------------------------------------------
class Stock:

  def __init__(self,name,code,per,pbr,rate):
    self.name = name
    self.code = code
    self.per = per
    self.pbr = pbr
    self.rate = rate

  def set_code(self, code):
    self.code = code

  def set_name(self,name):
    self.name = name

  def get_name(self):
    return self.name

  def get_code(self):
    return self.code

  def set_per(self,per):
    return self.per

  def set_pbr(self,pbr):
    return self.pbr

  def set_rate(self,rate):
    return self.rate
  
삼성 = Stock("삼성전자", "005930",'15.79','1.33','2.83')
print(삼성.name)
print(삼성.code)
print(삼성.get_name())
print(삼성.get_code())
삼성.set_per(12.75)
print(삼성.per)
#------------------------------------------
stock_list = []

삼성 = Stock("삼성전자", "005930",15.79, 1.33, 2.83)
현대차 = Stock('현대차', '005380', 8.70, 0.35, 4.27)
LG전자 = Stock('LG전자', '066570', 317.34, 0.69, 1.37)

stock_list.append(삼성)
stock_list.append(현대차)
stock_list.append(LG전자)

for a in stock_list:
  print(a.code, a.per)
