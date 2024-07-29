line = int(input('Tree height(5~30) : '))

if line < 5 or line > 30:
    print("Height must be between 5 and 30.")
else:
    # 트리의 윗부분 출력
    for i in range(1, line * 2, 2):
        print(" " * ((line * 2 - 1 - i) // 2) + "*" * i)

    # 트리의 줄기 부분 출력
    for o in range(3):
        print(" " * (line - 2) + "***")

def print_tree(n):
    # 나무의 윗부분 (삼각형 부분)
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

    # 나무의 아랫부분 (줄기 부분)
    for i in range(n // 3):
        print(' ' * (n - 1) + '*')

# 나무의 높이를 입력받습니다.
height = int(input("나무의 높이를 입력하세요: "))
print_tree(height)

print('------------------------------------------------')

# 다이아몬드

line = int(input("Diamond 의 길이를 입력하세요(2~30) : "))

for x in range(1, line * 2, 2):
    print((" " * ( (line * 2 - 1 - x) // 2 )) + ("*" * x))

for y in range(line * 2-3, 0, -2):
    print((" " * ( (line * 2 - 1 - y) // 2 )) + "*" * y)

def print_diamond(n):
    # 윗부분
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

    # 아랫부분
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# 다이아몬드의 높이를 입력받습니다.
height = int(input("다이아몬드의 높이를 입력하세요: "))
print_diamond(height)

print('------------------------------------------------')

# X모양 별 찍기
def print_x(n):
    if n % 2 == 0:
        print("X 모양을 만들려면 홀수 크기를 입력해야 합니다.")
        return

    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

# X 모양의 크기를 입력받습니다.
size = int(input("X 모양의 크기를 입력하세요 (홀수): "))
print_x(size)

print('------------------------------------------------')


import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    return bool(re.match(pattern, email))

email = input("이메일 주소를 입력하세요: ")
print(f"유효한 이메일 주소입니다!" if is_valid_email(email) else "유효하지 않은 이메일 주소입니다.")