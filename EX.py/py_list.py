'''리스트 선언/추가/삭제...'''
movie_rank = ['닥터 스트레인지','스플릿','럭키']
movie_rank.append('배트맨')
movie_rank.insert(1,'슈퍼맨')
del movie_rank[3]
del movie_rank[2:]
print(movie_rank)

'''리스트 합치기'''
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1 + lang2
print(langs)

'''리스트 최댓값/최소값'''
nums = [1, 2, 3, 4, 5, 6, 7]
print('max :', max(nums))
print('min :', min(nums))

'''리스트 합 출력'''
nums = [1, 2, 3, 4, 5]
print(sum(nums))

'''리스트에 저장된 데이터 갯수'''
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

'''리스트 평균'''
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))

'''리스트 슬라이싱'''
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
print(nums[1::2])

'''리스트 역슬라이싱'''
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[::2])
print(interest[0], interest[2])

'''리스트 join'''
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))
print('/'.join(interest))
print('\n'.join(interest))

'''리스트 split'''
string = "삼성전자/LG전자/Naver"
interest = string.split('/')
print(interest)

'''리스트 오름차순'''
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)