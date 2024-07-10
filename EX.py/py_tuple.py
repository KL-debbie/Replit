'''튜플 생성'''
my_variable = ('닥터 스트레인지','스플릿','럭키')
print(my_variable)
tuplee = (1,)
print(tuplee)

'''튜플을 리스트로'''
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)
print(data)

'''리스트를 튜플로'''
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)

'''튜플 언팩킹'''
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

'''튜플 = tuple(range(시작, 끝, 증가폭))'''
data = tuple(range(2,100,2))
print(data)