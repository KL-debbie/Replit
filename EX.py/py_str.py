'''문자열 인덱싱'''
letters = 'python'
print(letters[0],letters[2])

'''슬라이싱할 때 `시작인덱스:끝인덱스:오프셋`을 지정'''
string = "홀짝홀짝홀짝"
print(string[::2])

'''문자열 슬라이싱'''
license_plate = "24가 2210"
print(license_plate[-4:])

'''문자열 뒤집기'''
let = "PYTHON"
print(let[::-1])

'''문자열 치환'''
phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))
print(phone_number.replace("-",""))

change_str = 'abcdfe2a354a32a'
print(change_str.replace('a','A'))

string = 'abcd'
string.replace('b', 'B')
print(string)

'''문자열 다루기'''
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

'''문자열은 수정 불가능'''
lang = 'python'
""" lang[0] = 'P' """
print(lang)

'''문자열 합/곱/반복'''
a = "3"
b = "4"
print(a + b)

print('hi'*3)
print('-'*80)

t1 = 'python'
t2 = 'java'
t3 = t1 + ' ' + t2 + ' ' 
print(t3*3)

'''문자열 출력'''
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 : %s 나이 : %d" %(name1, age1))
print("이름 : %s 나이 : %d" %(name2, age2))


'''컴마제거 후 정수 변환'''
stock_num = "5,969,782,550"
num = int(stock_num.replace(',',''))
print(num)

'''공백 제거'''
data = "   삼성전자    "
print(data.strip())

'''대/소문자 변환'''
ticker = "btc_krw"
print(ticker.upper())

ticker = "BTC_KRW"
print(ticker.lower())

'''첫글자 대문자 변환'''
name = 'hello'
print(name.capitalize())

'''endswith 메서드'''
file_name = "보고서.xlsx"
print(file_name.endswith(('xlsx','xls')))
print(file_name.endswith(('xlsx')))

'''startswith'''
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

'''split메서드'''
a = "hello world"
print(a.split())

ticker = "btc_krw"
print(ticker.split('_'))

date = "2020-05-01"
print(date.split('-'))

'''strip메서드'''
data = "039490     "
print(data.rstrip())