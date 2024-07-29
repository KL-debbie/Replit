# 가격 단위
price_unit = 100


class texts:
    title = " #### 클래스 %s 자판기 입니다. ####"
    products = "%s : %s (%s원)"
    insert_coins = "동전을 넣어주세요 : "
    not_enough_coins = "동전이 부족합니다. \n거스름돈은 %s원 입니다. "
    select_product = "원하는 상품 선택하세요 : "
    select_fault = "잘못 눌렀습니다."
    products_out = "선택하신 상품 %s 입니다. 거스름돈은 %s원 입니다. \n감사합니다."
    exit_message = "거스름돈이 0원이므로 프로그램을 종료합니다."


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
                inputCoin = int(input(texts.insert_coins))
            except ValueError:
                # 값 잘못 입력 시 에러 메시지 출력
                print(texts.select_fault)
            else:
                self.selectProduct(inputCoin)

    def selectProduct(self, coin):
        description = ''

        for selection, item in Products.productType.items():
            price = self.getProValue(selection)
            description += selection + " : " + item + '(' + str(price) + '원)\n'

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
        return Products.productValue.get(product, 0)

    def getProductName(self, product):
        return Products.productType.get(product, '')

    def payment(self, coin, name, value):
        if coin >= value:
            change = coin - value
            print(texts.products_out % (name, int(change)))
            if change == 0:
                print(texts.exit_message)
                exit()
        else:
            print(texts.not_enough_coins % (int(coin)))


# 자판기 실행
vm = CoffeeVM()
vm.run()