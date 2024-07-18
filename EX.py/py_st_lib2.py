# functools 고차 함수와 관련된 함수 제공
# import functools           functools 모듈 전체 가져오기, functools. ~~
# from functools import ...  functools 모듈에서 특정 함수나 클래스 직접 가져오기
# reduce() 반복 가능한 객체의 요소에 차례대로 누적 적용하여 객체를 하나의 값으로 줄이는 함수
from functools import reduce

data = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, data)
print(result)  # 15 출력

# 최댓값 구하기
num_list = [3, 2, 8, 1, 6, 7]
max_num = reduce(lambda x, y: x if x > y else y, num_list)
print(max_num)  # 8 출력

#-----------------------------------------------------------------
# operator 함수
# 함수형 프로그래밍 지원을 위해 다양한 연산자를 함수 형태로 제공하는 모듈
# itemgetter 주어진 인텍스나 키에 해당하는 값을 반환하는 함수
from operator import itemgetter

# 튜플 형식, 인텍스 사용 정렬
students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]

# 나이순 정렬
result = sorted(students, key=itemgetter(1))
print(result)

# 딕셔너리 형식, 키 사용 정렬
students = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"name": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 17, "grade": 'B'},
]

result = sorted(students, key=itemgetter('age'))
print(result)

# 키값이 동일할 경우 다른 키를 기준으로 추가 정렬
# 요소들이 모두 다르면 단일 키로 충분하지만 동일 요소가 있을 가능성이 있다면 여러 키를 사용하여 추가 정렬 기준 설정
# 여러 인덱스 혹은 키 사용 정렬
data = [
  (1, 'apple', 3.5), 
  (1, 'banana', 2.0), 
  (3, 'cherry', 4.0)
]

# 첫 번째와 세 번째 요소를 기준으로 정렬
result= sorted(data, key=itemgetter(0, 2))
print(result)

# 특정 키 기준 정렬
data = [
    {'name': 'John', 'age': 25, 'salary': 50000},
    {'name': 'Jane', 'age': 22, 'salary': 60000},
    {'name': 'Dave', 'age': 22, 'salary': 55000}
]
# 'age'와 'salary' 키를 기준으로 정렬
sorted_data = sorted(data, key=itemgetter('age', 'salary'))
print(sorted_data)

from operator import attrgetter
# attrgetter() 함수는 특정 인덱스나 키에 해당하는 값을 반환
class Address:
    def __init__(self, city):
        self.city = city

class Person:
    def __init__(self, name, age, address, height):
        self.name = name
        self.age = age
        self.address = address
        self.height = height

people = [
    Person('Alice', 30, Address('New York'), 165),
    Person('Bob', 25, Address('Los Angeles'), 180),
    Person('Charlie', 35, Address('Chicago'), 177)
]

# 나이로 정렬
sorted_people = sorted(people, key=attrgetter('age'))

for person in sorted_people:
    print(person.name, person.age)
print('-----------------')   

# 나이와 키로 정렬
sorted_people = sorted(people, key=attrgetter('age', 'height'))

for person in sorted_people:
    print(person.name, person.age, person.height)
print('-----------------')   

# 도시 이름으로 정렬
sorted_people = sorted(people, key=attrgetter('address.city'))

for person in sorted_people:
    print(person.name, person.age, person.address.city)

#-----------------------------------------------------------------
