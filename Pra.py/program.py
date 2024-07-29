# 성적, 학점 입력받아 졸업 여부 확인
'''
graduation, score = map(float, input('졸업학점과 이수학점 입력 : ').split())

if graduation >= 2.0 and score >= 140:
  print('졸업 가능')
elif graduation < 2.0 and score >=140:
  print('졸업학점 부족')
elif graduation >= 2.0 and score < 140:
  print('이수학점 부족')
else :
  print('둘다 부족, 졸업 불가')
'''

# 출생년도 입력 받아 재난지원금 신청 가능 요일
'''
str = input('출생년도 입력 :')
if str[3] == '1' or str[3] == '6':
  print('Monday')
elif str[3] == '2' or str[3] == '7':
  print('Tuesday')
elif str[3] == '3' or str[3] == '8':
  print('Wednesday')
elif str[3] == '4' or str[3] == '9':
  print('Thursday')
elif str[3] == '5' or str[3] == '0':
  print('Friday')
'''

# 가위바위보
'''
import random
coint = 0

while True:
  rn = random.randint(1,3)
  if rn == 1:
    com = '가위'
  elif rn == 2:
    com = '바위'
  elif rn == 3:
    com = '보'

  player = input('가위, 바위, 보 중 하나 입력')
'''

import random

def get_computer_choice():
    choices = ['가위', '바위', '보']
    return random.choice(choices)

def get_user_choice():
    user_input = input("가위, 바위, 보 중 하나를 선택하세요: ")
    while user_input not in ['가위', '바위', '보']:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        user_input = input("가위, 바위, 보 중 하나를 선택하세요: ")
    return user_input

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "비겼습니다!", None
    elif (user_choice == '가위' and computer_choice == '보') or \
         (user_choice == '바위' and computer_choice == '가위') or \
         (user_choice == '보' and computer_choice == '바위'):
        return "사용자가 이겼습니다!", "user"
    else:
        return "컴퓨터가 이겼습니다!", "computer"

def play_game():
    print("가위바위보 게임에 오신 것을 환영합니다!")
    user_wins = 0
    computer_wins = 0

    while user_wins < 3 and computer_wins < 3:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"사용자 선택: {user_choice}")
        print(f"컴퓨터 선택: {computer_choice}")
        result, winner = determine_winner(user_choice, computer_choice)
        print(result)

        if winner == "user":
            user_wins += 1
        elif winner == "computer":
            computer_wins += 1

        print(f"현재 점수 - 사용자: {user_wins}, 컴퓨터: {computer_wins}")

    if user_wins == 3:
        print("사용자가 최종 승리했습니다!")
    else:
        print("컴퓨터가 최종 승리했습니다!")

if __name__ == "__main__":
    play_game()