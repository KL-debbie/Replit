'''
def profile(name, age, main_lang):
  print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
profile('dk',27,'java')
'''
#-----------------------------------------------------------------------
'''
def profile(name, age= 17, main_lang='python'):
  print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile('dk')
profile('wo')
'''
#-----------------------------------------------------------------------
'''
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
  print("name :{0}\tage :{1}\t".format(name,age), end="")
  print(lang1, lang2, lang3, lang4, lang5)

profile('dk', 12, "pt", 'java','c','c++',"c#")
profile('k', 12, "pt", 'java','c','',"")
'''
#-----------------------------------------------------------------------
'''
gun = 10

def checkpoint(soldiers):   #경계근무
  global gun  # 전역 공간에 있는 gun사용(밖에 정의된 gun)
  gun = gun - soldiers
  print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
  gun = gun - soldiers
  print("[함수 내] 남은 총 : {0}".format(gun))
  return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2)  # 경계 근무 2명이 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
'''
#-----------------------------------------------------------------------
'''
def std_weight(height, gender):
  if gender == "남자":
    return height * height * 22
  else:
    return height * height * 21

height = 175    # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender, weight))
'''
#-----------------------------------------------------------------------
'''
import sys
print('python','java', file = sys.stdout)
print('python','java', file = sys.stderr)
'''
#-----------------------------------------------------------------------
# 시험 성적, 왼쪽& 오른쪽 정렬
scores = {'수학': 0, '영어': 50, '국어':100}
for subject, score in scores.items():
  # print(subject, score)
  print(subject.ljust(5), str(score).rjust(4), sep=":")

#-----------------------------------------------------------------------
# 은행 대기 순번표 001, 002, ----
for num in range(1, 21):
  print("대기번호: " + str(num).zfill(3))

#-----------------------------------------------------------------------
# answer = input("값 입력 : ")
# print('입력 값은 ' +answer)

#-----------------------------------------------------------------------
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬 하되, 총 10자리 공간 확보
print("{0: >10}".format(500))    # 500 출력

# 양수일 때 +, 음수일 때 - 표시
print( "{0: >+10}".format(500))
print( "{0: >+10}".format(-500))

# 왼쪽 정렬, 빈칸을 _로 채우기
print( "{0:_<+10}".format(500))

# 3자리마다 , 찍기
print("{0:,}".format(10000000000000))

# 3자리마다 , 찍기, +- 부호도 붙이기
print("{0:+,}".format(10000000000000))
print("{0:,}".format(-10000000000000))

# 3자리마다 , 찍기, +- 부호도 붙이기, 자릿수 확보
# 빈자리는 ^로 채우기
print("{0:^<+40,}".format(900000000))

# 소수점 출력
print("{0:f}".format(5/6))

# 소수점 특정 자리수까지 표시
print("{0:.2f}".format(5/3))
