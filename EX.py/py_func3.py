def make_url(url):
  print('www.'+url+'.com')

'''return 사용 시 결과는 print(함수)'''
make_url("naver")
#---------------------------------
def make_list(str):
  return list(str)

print(make_list('abcd'))
#---------------------------------
def pickup_even(num_list):
  res=[]
  for a in num_list:
    if a % 2 ==0:
      res.append(a)
  return res
print(pickup_even([3,4,5,6,7,8]))
#---------------------------------
def convert_int(num_list):
  return int(num_list.replace(",",""))

print(convert_int('1,2334'))
#---------------------------------
def 함수(num) :
  return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)
#---------------위 함수랑 동일(축약한 것)----------------
def 함수1(num) :
  return num + 4

c = 함수1(함수1(함수1(10)))
print(c)
#---------------------------------
