'''for문'''
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)

과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")

for 변수 in ["A", "B", "C"]:
  print("출력:", 변수)

변수 = "A"
print("출력:", 변수)
변수 = "B"
print("출력:", 변수)
변수 = "C"
print("출력:", 변수)

변수 = "A"
b = 변수.lower()
print("변환:", b)
변수 = "B"
b = 변수.lower()
print("변환:", b)
변수 = "C"
b = 변수.lower()
print("변환:", b)

for 변수 in [10,20,30]:
  print(변수)

for a in [10,20,30]:
  print(a)

for num in [10,20,30]:
  print(num)
  print('-------')

for num in [10,20,30,40]:
  print('-------')

리스트 = [100, 200, 300]
for a in 리스트:
  print(a+ 10)

리스트 = ["김밥", "라면", "튀김"]
for a in 리스트:
  print('오늘의 메뉴 : ', a)

'''길이'''
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for a in 리스트:
  print(len(a))

리스트 = ['dog', 'cat', 'parrot']
for a in 리스트:
  print(a, len(a))
  print(a[0])

'''곱셈 표현하기'''
리스트 = [1, 2, 3]
for a in 리스트:
  print( '3 x', a)

for a in 리스트:
  print( '3 x', a, '=', 3*a)

'''바인딩'''
리스트 = ["가", "나", "다", "라"]
b = 리스트[1:]
for a in b:
  print(a)

b = 리스트[::2]
for a in b:
  print(a)

b = 리스트[::-1]
for a in b:
  print(a)