a = range(0, 100)
for b in a:
  print(b)

a = range(2002, 2050, 4)
for b in a:
  print(b)

a = range(3, 31, 3)
for b in a:
  print(b)

for a in range(100):
  print(99 - a)

for a in range(10):
  print(a / 10)

#구구단 표현
for a in range(1, 10):
  print('3x', str(a), '=', 3 * a)

for a in range(1, 10):
  if a % 2 == 1:
    print('3x', str(a), '=', 3 * a)

#합 곱
sum = 0
for a in range(1, 11):
  sum += a
print('합 :', sum)

sum = 0
for a in range(1, 11, 2):
  sum += a
print('합 :', sum)

dou = 1
for a in range(1, 11):
  dou *= a
print(dou)

#리스트 출력
price_list = [32100, 32150, 32000, 32500]
for a in range(len(price_list)):
  print(price_list[a])

for a in range(len(price_list)):
  print(a, price_list[a])

for a in range(len(price_list)):
  print(3 - a, price_list[a])

for a in range(len(price_list)):
  print(a * 10 + 90, price_list[a])

#리스트 출력 2
my_list = ["가", "나", "다", "라"]
# for a in range(len(my_list)-1):
for a in range(0, 3):
  print(my_list[a], my_list[a + 1])
# my_list[a] = 0, my_list[a+1] = 1

for i in range(len(my_list) - 1):
  print(my_list[len(my_list) - 1 - i], my_list[len(my_list) - 2 - i])

my_list = ["가", "나", "다", "라", '마']
# for a in range(1, len(my_list)-1):
for a in range(0, 3):
  print(my_list[a], my_list[a + 1], my_list[a + 2])

my_list = [100, 200, 400, 800]
for a in range(0, 3):
  print(my_list[a + 1] - my_list[a])

my_list = [100, 200, 400, 800, 1000, 1300]
for a in range(0, 4):
  sum = my_list[a] + my_list[a + 1] + my_list[a + 2]
  print(sum / 3)

# 변동폭 구하기
low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for a in range(0, 5):  # 0~4
  diff = high_prices[a] - low_prices[a]
  volatility.append(diff)
print(volatility)

