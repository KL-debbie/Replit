# 비밀번호 강도 체크
'''
import re

def check_password_strength(password):
    if len(password) < 8:
        return "비밀번호가 너무 짧습니다."
    if not re.search("[a-z]", password):
        return "소문자를 포함해주세요."
    if not re.search("[A-Z]", password):
        return "대문자를 포함해주세요."
    if not re.search("[0-9]", password):
        return "숫자를 포함해주세요."
    if not re.search("[@#$%^&+=]", password):
        return "특수 문자를 포함해주세요."
    return "비밀번호가 안전합니다."

while True:
    password = input("비밀번호를 입력하세요: ")
    result = check_password_strength(password)
    print(result)
    if result == "비밀번호가 안전합니다.":
        break
print('------------------------------------------------')

# Email 유효성 체크

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    return bool(re.match(pattern, email))

while True:
    email = input("이메일 주소를 입력하세요: ")
    if is_valid_email(email):
        print("유효한 이메일 주소입니다!")
        break
    else:
        print("유효하지 않은 이메일 주소입니다. 다시 시도해주세요.")

print('------------------------------------------------')
'''
filename = "Pra.py/sample.txt"

# 시도할 인코딩 목록
encodings = [
    'utf-8', 'latin-1', 'cp1252', 'iso-8859-1', 'utf-16', 'utf-32', 'ascii',
    'utf-16-le', 'utf-16-be', 'utf-32-le', 'utf-32-be'
]
lines = []

# 여러 인코딩을 시도하여 파일 읽기
for encoding in encodings:
    try:
        with open(filename, 'r', encoding=encoding) as file:
            lines = file.readlines()
        print(f"파일을 {encoding} 인코딩으로 성공적으로 읽었습니다.")
        break
    except UnicodeDecodeError:
        print(f"파일을 {encoding} 인코딩으로 읽을 수 없습니다.")
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {filename}")
        break

# 파일을 성공적으로 읽었는지 확인
if lines:
    while True:
        word_to_search = input("검색할 단어를 입력하세요: ")
        found = False
        for line_number, line in enumerate(lines, 1):
            if word_to_search in line:
                print(f"{line_number}번째 줄: {line.strip()}")
                found = True
        if not found:
            print("찾는 단어가 없습니다. 다시 검색해 주세요.")
        else:
            break
else:
    print("파일을 읽을 수 있는 인코딩을 찾지 못했습니다.")
