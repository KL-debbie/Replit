#
'''
import random

num = int(input("lotto 게임 수를 입력하세요 : "))

print("lotto 자동 번호 입니다.")
print("----------------------")
# 입력한 게임 수 만큼 반복
for x in range(1, num+1):
    lotto = [0, 0, 0, 0, 0, 0]

    lotto[0] = random.randrange(1, 46, 1)

    lotto[1] = lotto[0]
    lotto[2] = lotto[0]
    lotto[3] = lotto[0]
    lotto[4] = lotto[0]
    lotto[5] = lotto[0]

    # 중복된 수가 발생되지 않도록 채번
    while (lotto[0] == lotto[1]):
        lotto[1] = random.randrange(1, 46, 1)
    while (lotto[0] == lotto[2] or lotto[1] == lotto[2]):
        lotto[2] = random.randrange(1, 46, 1)
    while (lotto[0] == lotto[3] or lotto[1] == lotto[3] or lotto[2] == lotto[3]):
        lotto[3] = random.randrange(1, 46, 1)
    while (lotto[0] == lotto[4] or lotto[1] == lotto[4] or lotto[2] == lotto[4] or lotto[3] == lotto[4]):
        lotto[4] = random.randrange(1, 46, 1)
    while (lotto[0] == lotto[5] or lotto[1] == lotto[5] or lotto[2] == lotto[5] or lotto[3] == lotto[5] or lotto[4] == lotto[5]):
        lotto[5] = random.randrange(1, 46, 1)

    # 결과를 정렬
    lotto.sort()

    # 결과 출력
    print(lotto)
'''

import random

def generate_lotto_numbers():
    # 1부터 45까지의 숫자 중에서 6개를 랜덤으로 선택 (중복 없음)
    numbers = random.sample(range(1, 46), 6)
    # 선택된 숫자들을 정렬
    numbers.sort()
    return numbers

def main():
    try:
        num = int(input("로또 게임 수를 입력하세요: "))
        if num <= 0:
            print("게임 수는 1 이상의 정수를 입력해야 합니다.")
            return

        print("로또 자동 번호입니다.")
        print("----------------------")

        # 입력한 게임 수 만큼 반복
        for _ in range(num):
            lotto_numbers = generate_lotto_numbers()
            print(lotto_numbers)

    except ValueError:
        print("유효한 숫자를 입력하세요.")

if __name__ == "__main__":
    main()

