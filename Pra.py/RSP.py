# 가위바위보 게임...

import random

def get_computer_choice():
    choices = ['가위', '바위', '보']
    return random.choice(choices)

def get_user_choice():
    user_input = input("가위, 바위, 보 중 하나를 선택하세요: ")
    while user_input not in ['가위', '바위', '보']:
        print("잘못된 입력입니다. 다시 선택해주세요.")
        user_input = input("가위, 바위, 보 중 하나를 선택하세요: ")
    return user_input

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "비겼습니다!"
    elif (user_choice == '가위' and computer_choice == '보') or \
         (user_choice == '바위' and computer_choice == '가위') or \
         (user_choice == '보' and computer_choice == '바위'):
        return "사용자가 이겼습니다!"
    else:
        return "컴퓨터가 이겼습니다!"

def play_game():
    print("가위바위보 게임에 오신 것을 환영합니다!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"사용자 선택: {user_choice}")
    print(f"컴퓨터 선택: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
