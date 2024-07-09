'''print'''
print("Hello World")
print("Mary's cosmetics")
print('신씨가 소리질렀다. "도둑이야".')
print('C:\Windows')

'''sep 사용'''
print('naver','kakao','sk','samsung',sep=';')
print('naver','kakao','sk','samsung',sep='/')

'''줄바꿈 표시할 경우 사용'''
print("first", end="")
print("second")

'''연산'''
print(5/3)
print(2+2*3)

'''변수'''
ss = 50000
money = ss * 10
print(money)

'''문자 연결'''
s = "hello"
t = "python"
print(s +'! ' + t)

'''타입 확인'''
a = "132"
print(type(a))

'''숫자를 문자로 변환'''
nstr = "720"
nint = int(nstr)
print(nint, type(nint))

'''문자를 숫자로 변환'''
num = 100
n = str(num)
print(n, type(n))

'''문자를 실수로 변환'''
n = '15.79'
num = float(n)
print(num, type(num))

'''문자를 정수로 변환'''
year = '2020'
nyear = int(year)
print(nyear-1, nyear-2, nyear-3)
