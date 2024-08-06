from collections import defaultdict
from datetime import datetime

todo_list = defaultdict(list)

def add_task():
    date = datetime.now().strftime("%Y-%m-%d")
    task = input("추가할 할 일을 입력하세요: ")
    todo_list[date].append(task)
    print(f"'{task}'가 {date}의 할 일 목록에 추가되었습니다.")

def view_tasks():
    if not todo_list:
        print("\n할 일 목록이 비어 있습니다.")
        return

    print("\n할 일 목록:")
    for date, tasks in todo_list.items():
        print(f"\n{date}:")
        for idx, task in enumerate(tasks, 1):
            print(f"  {idx}. {task}")

def remove_task():
    date = input("삭제할 할 일이 있는 날짜를 입력하세요 (YYYY-MM-DD): ")
    if date not in todo_list:
        print(f"{date}에 할 일이 없습니다.")
        return

    print(f"\n{date}의 할 일 목록:")
    for idx, task in enumerate(todo_list[date], 1):
        print(f"  {idx}. {task}")

    try:
        idx = int(input("삭제할 할 일의 번호를 입력하세요: "))
        if 1 <= idx <= len(todo_list[date]):
            removed_task = todo_list[date].pop(idx - 1)
            print(f"'{removed_task}'가 {date}의 할 일 목록에서 삭제되었습니다.")
            if not todo_list[date]:  # 날짜의 할 일이 모두 삭제되면 날짜도 삭제
                del todo_list[date]
        else:
            print("올바르지 않은 번호입니다.")
    except ValueError:
        print("올바른 숫자를 입력하세요.")

if __name__ == "__main__":
    while True:
        choice = input("\n1: 할 일 추가, 2: 할 일 조회, 3: 할 일 삭제, 4: 종료 \n선택하세요: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            break
        else:
            print("올바른 선택이 아닙니다.")