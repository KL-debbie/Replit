# 자판기 만들기 실습

# 가격 단위
price_unit = 100


class texts:
  title = " #### 클래스 %s 자판기 입니다. ####"
  products = "%s : %s ($s원)"
  insert_coins = "동전을 넣어주세요 : "
  nenough_coins = "동전이 부족합니다. \n거스름돈은 %s원 입니다. "
  select_product = "원하는 상품 선택하세요 : "
  select_fault = "잘못 눌렀습니다."
  products_out = "선택하신 상품 %s 입니다. 거스름돈은 %s원 입니다. \n감사합니다."


class Products:
  productType = {'1': '설탕커피', '2': '프림커피', '3': '원두커피'}
  productValue = {'1': 200, '2': 300, '3': 400}


class CoffeeVM(Products):
  _name = '커피'

  def __init__(self):
    print(texts.title % self._name)

  def run(self):
    while True:
      try:
        inputCoin = float(input(texts.insert_coins))
      except ValueError:
        # 값 잘못 입력 시 에러 메시지 출력
        print(texts.select_fault)
      else:
        self.selectProduct(inputCoin)

  def selectProduct(self, coin):
    description  = ''

    for selection, item in Products.productType.items():
      price = self.getProValue(selection)
      description += selection + " : " + item + '(' + str(price) + '원)'

    print(description)
    inputProduct = input(texts.select_product)
    productValue = self.getProValue(inputProduct)

    if productValue:
      productName = self.getProductName(inputProduct)
      self.payment(coin, productName, productValue)
    else:
      print(texts.select_fault)
      self.selectProduct(coin)

  def getProValue(self, product):
    returnVal = 0
    for selection, value in Products.productValue.items():
      if selection == product:
        returnVal = value
    return returnVal

  def getProductName(self, product):
    for selection, name in Products.productType.items():
      if selection == product:
        return name

  def payment(self, coin, name, value):
    coinValue = coin * price_unit
    if coinValue >= value:
      change = coinValue - value
      print(texts.products_out % (name, int(change)))
    else:
      print(texts.nenough_coins % (int(coinValue)))


