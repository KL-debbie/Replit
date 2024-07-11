def print_reverse(str):
  print(str[::-1])

print_reverse('python')
# ----------------------------------------
def print_score(sco_list):
  print(sum(sco_list) / len(sco_list))

print_score([3,4,5])
# ----------------------------------------
def print_even(num_list):
  for a in num_list:
    if a % 2 == 0:
      print(a)
      
print_even([1,3,2,5,55,3567])
# ----------------------------------------
def print_keys(dic):
  for keys in dic.keys():
    print(keys)

print_keys({"이름":"김말똥", "나이":30, "성별":0})
# ----------------------------------------
my_dict = {
  "10/26" : [100, 130, 100, 100],
  "10/27" : [10, 12, 10, 11]
  }

def print_value_by_key(my_dict, key):
    print(my_dict[key])

print_value_by_key(my_dict, "10/26")
# ----------------------------------------
def print_5xn1(str):
  times = int(len(str) / 5)
  for a in range(times+1):
    print(str[5*a: 5*a+5])

print_5xn1("아이엠어보이유알어걸하하하하")

def print_5xn(str, num):
  times = int(len(str) /3)
  for a in range(times+1):
    print(str[3*a: 3*a+3])

print_5xn("아이엠어보이유알어걸하하하하호아이리아", 3)
# ----------------------------------------
def calc_monthly_salary(annual_salary):
  print(int(annual_salary / 12))

calc_monthly_salary(1200000)
# ----------------------------------------
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)