# 문제 해결 시간
'''
time = int(input("해결 시간 ? "))

min = time // 60
sec = time % 60
print(f"{min}분 {sec}초 만에 문제 해결")
'''

# 원 넓이
'''
r = float(input('반지름 입력 : \n'))

area = r**2 * 3.14
cir_round = r * 2 * 3.14
print(f"원의 넓이 : {area}")
print(f"원의 둘레 : {cir_round}")
'''

# 비밀번호 - 잠금해제
'''
passwd = "a1234!"
pwd = input(str('비밀번호를 입력하세요 : \n'))

if pwd == passwd:
  print('비밀번호가 일치합니다. 잠금 해제')
else:
  print('비밀번호 오류, 다시 입력하세요')
  '''

# BMI 구하기
'''
height = float(input("키 입력하세요 : \n"))
weight = float(input("몸무게 입력하세요 : \n"))

bmi = weight / ((height/100) ** 2)

if bmi < 18.5:
  print("저체중")
elif bmi >= 18.5 and bmi < 23:
  print("정상")
elif bmi >= 23 and bmi < 24.9:
  print("과체중")
elif bmi >= 25 and bmi < 29.9:
  print("경도 비만")
elif bmi >= 30 and bmi < 34.9:
  print("중등도 비만")
else:
  print("고도 비만")
  '''

# 커피 자판기
'''
print("1 : 아메리카노")
print("2 : 카페라떼")
print("3 : 핫초코")

coffee = int(input("커피 종류를 선택하세요 : \n"))
coffee_price = 0
if coffee == 1:
  coffee_price = 1800
elif coffee == 2:
  coffee_price = 2700
else:
  coffee_price = 2300

cups = int(input("몇 잔을 드릴까요? : \n"))
total_price = coffee_price * cups

input_money = int(input(f"총 금액은 {total_price}원, 돈 투입해주세요 \n"))

if input_money >= total_price:
  change = input_money - total_price
  print(f"거스름돈은 {change}원 입니다")
else:
  print("금액이 부족하므로 주문 취소됩니다.")
'''

# 구구단
'''
print('구구단~~~~')

num = int(input('몇 단 출력할까유~   \n'))

for i in range(1, 10):
  print(f'{num} * {i} = {num * i}')
'''

# 사전
'''
dict_es = {'señora':'아가씨', 'madre':'엄마', 'cuchillo':'나이프', 'gazpacho':'토마토냉스프', 'pollo asado':'닭구이', 'vino tinto':'적포도주', 'helado':'아이스크림', 'huevo frito':"계란 후라이", 'padre':'아빠'}

for i in dict_es:
  user_input = input(f"{i}의 뜻은? \n")

  if user_input == dict_es[i]:
    print("정답입니다")
  else:
    print(f"오답입니다. 정답은 {dict_es[i]} 입니다")
'''

# 행맨
'''
dict_es = ['señora', 'madre', 'cuchillo', 'gazpacho', 'pollo asado', 'vino tinto', 'helado', 'huevo frito', 'padre']

import random

answer = random.choice(dict_es)
guessLetter = list('_'*len(answer))               
life = 3
game_over = False

while not game_over:
  print(f"chance : {life}")
  user_guess = input('한 글자씩 추측').lower()

  if len(user_guess) == 1 and user_guess.isalpha():
    for i in range(len(answer)):
      if answer[i] == user_guess:
        guessLetter[i] = user_guess
    print(guessLetter)
    if '_' not in guessLetter:
      print("정답입니다")
      game_over = True

    if user_guess not in answer:
      life -= 1
      if life == 0:
        game_over = True
        print(f"Fali answer is {answer}")
  else:
    print('한 글자씩 입력 ')
 '''

# 꽃 그리기
'''
import turtle as t

t.speed(0)

# 꽃잎 한장 표현
def petal():
  for i in range(2):
    t.circle(150,110)
    t.left(70)

# 꽃 만들기
def d_flower():
  t.color('pink')
  t.begin_fill()
  for i in range(6):
    petal()
    t.left(360/6)
  t.end_fill
  # 꽃 수술 표현
  t.goto(0,-30)
  t.color('deeppink')
  t.begin_fill()
  t.circle(30)
  t.end_fill()

t.ht()
t.bgcolor('lightblue')
d_flower()
'''

# 그림판 만들기
'''
import tkinter as tk

def paint(event):
    x1, y1 = event.x - 1, event.y - 1
    x2, y2 = event.x + 1, event.y + 1
    if eraser_mode:
        canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='white', width=pen_size)
    else:
        canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline=pen_color, width=pen_size)

def blue():
    global pen_color
    pen_color = 'blue'

def cg_color(color):
    global pen_color
    pen_color = color

def size_up():
    global pen_size
    pen_size += 1

def size_down():
    global pen_size
    if pen_size > 1:
        pen_size -= 1

def toggle_eraser():
    global eraser_mode
    eraser_mode = not eraser_mode

pen_color = "black"
pen_size = 1
eraser_mode = False

window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500, bg='white')
canvas.pack()
canvas.bind("<B1-Motion>", paint)

button_b = tk.Button(window, text="파랑", width=5, bg='lightblue', command=blue, font=('나눔바른펜', 12))
button_b.place(x=0, y=0)

button_p = tk.Button(window, text="핑크", width=5, bg='pink', command=lambda: cg_color("pink"), font=('나눔바른펜', 12))
button_p.place(x=0, y=40)

button_r = tk.Button(window, text="빨강", width=5, bg='red', command=lambda: cg_color("red"), font=('나눔바른펜', 12))
button_r.place(x=0, y=80)

button_sizeup = tk.Button(window, text="bold", command=size_up)
button_sizeup.place(x=0, y=120)

button_sizedown = tk.Button(window, text="thin", command=size_down)
button_sizedown.place(x=0, y=160)

button_eraser = tk.Button(window, text="지우개", command=toggle_eraser)
button_eraser.place(x=0, y=200)

window.mainloop()
'''

# 클릭 박스 만들기
'''
import tkinter as tk

def check_result():
  if checked.get() == True:
    label.config(text='Clicked!!!', font=('나눔바른펜', 20, 'bold'))
  else:
    label.config(text='No Clicked!!!', font=('나눔바른펜', 20, 'bold'))

    

window = tk.Tk()  # tk()가 아닌 tk.Tk()를 사용해야 합니다.
window.title("checkBox")
window.geometry('300x300')

checked = tk.BooleanVar()
check_btn = tk.Checkbutton(window, text="checkbox", variable=checked, command=check_result)

check_btn.pack()
label =tk.Label(window, text='')
label.pack()

window.mainloop()
'''
