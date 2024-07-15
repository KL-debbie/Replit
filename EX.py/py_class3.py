class car:    # class 정의
  def __init__(self,wheel,price):
    self.wheel = wheel
    self.price = price

  def info(self):
    print('wheel :', self.wheel)
    print('price :', self.price)

class my_car(car):        # car 클래스 상속
  def __init__(self,wheel,price, move):
    self.wheel = wheel
    self.price = price
    self.move = move

class my_bike(car):      # car 클래스 상속
  def __init__(self, wheel, price, move):
    super().__init__(wheel, price)
    self.move = move

  def info(self):        # 구동계 정보 출력
    super().info()
    print('move :', self.move)
    
#-----------------------------------------------    
car1 = car(2, 1000)
print(car1.wheel)
print(car1.price)
#-----------------------------------------------    
car1 = car(2, 1000)
car1.info()
#-----------------------------------------------
car2 = my_car(2, 100, '자전거')
print(car2.wheel)
print(car2.move)
#-----------------------------------------------
bike = my_bike(2, 100,'시마노')
bike.info()
