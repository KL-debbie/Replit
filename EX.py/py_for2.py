리스트 = [3, -20, -3, 44]
for a in 리스트:
  if a < 0:
    print(a)

리스트 = [3, 100, 23, 44]
for a in 리스트:
  if a % 3 == 0:
    print(a)

리스트 = [13, 21, 12, 14, 30, 18]
for a in 리스트:
  if a % 3 == 0 and a < 20:
    print(a)

리스트 = ["I", "study", "python", "language", "!"]
for a in 리스트:
  if len(a) >= 3:
    print(a)

리스트 = ["A", "b", "c", "D"]
for a in 리스트:
  if a.isupper():
    print(a)

리스트 = ['dog', 'cat', 'parrot']
for a in 리스트:
  print(a[0].upper() + a[1:])

리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for a in 리스트:
  b = a.split('.')
  print(b[0])

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for a in 리스트:
  b = a.split('.')
  if b[1] == 'h':
    print(a)

