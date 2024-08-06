import os

def write_diary():
    date = input("날짜를 입력하세요 (YYYY-MM-DD): ")
    content = input("일기 내용을 작성하세요:\n")
    # 현재 스크립트의 디렉토리 경로를 가져옵니다.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, f"{date}.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"{date} 일기가 저장되었습니다.")

def read_diary():
    date = input("조회할 날짜를 입력하세요 (YYYY-MM-DD): ")
    # 현재 스크립트의 디렉토리 경로를 가져옵니다.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, f"{date}.txt")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"\n{date} 일기 내용:\n{content}")
    except FileNotFoundError:
        print(f"{date}에 작성된 일기가 없습니다.")

while True:
    choice = input("\n1: 일기 작성, 2: 일기 조회, 3: 종료 \n선택하세요: ")
    if choice == "1":
        write_diary()
    elif choice == "2":
        read_diary()
    elif choice == "3":
        break
    else:
        print("올바른 선택이 아닙니다.")