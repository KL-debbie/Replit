# try-except만 쓰는 방법
# 발생 오류만 포함 except문
# 발생 오류와 오류 변수 포함 except문

'''
* try 블록

예외가 발생할 가능성이 있는 코드를 포함합니다.

* except 블록

try 블록에서 예외가 발생했을 때 실행할 코드를 포함합니다.
특정 예외를 지정할 수 있으며, 여러 개의 except 블록을 사용할 수 있습니다.

* else 블록

try 블록에서 예외가 발생하지 않았을 때 실행할 코드를 포함합니다.
선택적으로 사용할 수 있습니다.

* finally 블록

예외 발생 여부와 상관없이 항상 실행할 코드를 포함합니다.
선택적으로 사용할 수 있습니다.
'''
#--------------------------------------------------------------
# 기본 예제
try:
  # 예외가 발생할 가능성이 있는 코드
  result = 4 / 0
except ZeroDivisionError as e:  # 예외가 발생했을 때 실행할 코드
  print(e)
else:        # 예외가 발생하지 않았을 때 실행할 코드
  print('result : ', result)
finally:      # 예외 발생 여부와 상관없이 항상 실행할 코드
  print('Finish')
#--------------------------------------------------------------
# 여러 예외 처리
try:
  # 예외가 발생할 가능성이 있는 코드
  v = int(input('Number : '))
  result = 4 / v
except ValueError:              # 예외가 발생했을 때 실행할 코드
  print('Number!!!!!')
except ZeroDivisionError as e:  # 예외가 발생했을 때 실행할 코드
  print(e)
else:        # 예외가 발생하지 않았을 때 실행할 코드
  print('result : ', result)
finally:      # 예외 발생 여부와 상관없이 항상 실행할 코드
  print('Finish')
#--------------------------------------------------------------
# 모든 예외 처리
try:
    # 예외가 발생할 가능성이 있는 코드
    result = 10 / 0
except:
    # 모든 예외를 처리
    # 특정 예외를 명시적으로 처리 또는 일반적인 예외는 Exception 클래스 사용하여 처리하는 것이 좋음
    print("예외가 발생했습니다.")
finally:
    print("예외 처리를 완료했습니다.")
#--------------------------------------------------------------
# try-else-if 
try:
  value = int(input("숫자를 입력하세요: "))
except ValueError:
  print("유효한 숫자를 입력하세요.")
else:
  if value > 0:
      print("입력한 숫자는 양수입니다.")
  elif value < 0:
      print("입력한 숫자는 음수입니다.")
  else:
      print("입력한 숫자는 0입니다.")
finally:
  print("프로그램을 종료합니다.")