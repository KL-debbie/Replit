import random

def generate_random_number():
    rn = ["", "", ""]
    rn[0] = str(random.randint(1, 9))
    while (rn[0] == rn[1]):
        rn[1] = str(random.randint(1, 9))
    while (rn[0] == rn[2] or rn[1] == rn[2]):
        rn[2] = str(random.randint(1, 9))
    return rn

def main():
    rn = generate_random_number()
    t_cnt = 0  # 시도횟수
    s_cnt = 0  # 스트라이크 갯수
    b_cnt = 0  # 볼 갯수

    print("숫자야구게임을 시작합니다 !!!")
    print("---------------------------")
    while s_cnt < 3:
        num = input("숫자 3자리를 입력하세요 : ")

        if len(num) != 3 or not num.isdigit():
            print("잘못된 입력입니다. 숫자 3자리를 입력하세요.")
            continue
            12
        s_cnt = 0
        b_cnt = 0

        for i in range(3):
            for j in range(3):
                if num[i] == rn[j]:
                    if i == j:
                        s_cnt += 1
                    else:
                        b_cnt += 1

        print(f"결과 : [{s_cnt}] Strike [{b_cnt}] Ball")
        t_cnt += 1

    print("---------------------------")
    print(f"{t_cnt}번 만에 정답을 맞추셨습니다.")

if __name__ == "__main__":
    main()