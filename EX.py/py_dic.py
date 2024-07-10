'''딕셔너리 별 표현식 - 좌측 n개 값만 바인딩'''
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores
print(valid_score)
'''딕셔너리 별 표현식 - 우측 n개 값만 바인딩'''
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores
print(valid_score)
'''딕셔너리 별 표현식 - 가운데 n개 값만 바인딩'''
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score, b = scores
print(valid_score)
'''딕셔너리 생성/추가/n개 출력/수정'''
temp = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
temp['죠스바'] = 1200
temp['월드콘'] = 1500
temp['메로나'] = 1300
del temp['메로나']
print(temp)
print('폴라포 가격 : ', temp['폴라포'])
'''딕셔너리 인덱싱'''
inventory = {
    'melona': [300, 20],
    'vivic': [400, 3],
    'jaws_bar': [250, 100],
}

inventory['월드콘'] = [500, 7]
print(inventory)
print(inventory['melona'][0], '원')
print(inventory['melona'][1], '개')
'''딕셔너리 keys() / values() 메서드'''
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.keys())
price = list(icecream.values())
print(ice)
print(price)
'''딕셔너리 update 메서드'''
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수': 2700, '아맛나': 1000}
icecream.update(new_product)
print(icecream)
'''zip과 dict'''
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)
