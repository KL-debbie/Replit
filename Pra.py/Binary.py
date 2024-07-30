def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# 배열 입력 받기
arr_input = input("배열을 입력하세요 (공백으로 구분된 숫자들): ")
arr = list(map(int, arr_input.split()))

# 배열 정렬 (이진 탐색을 위해 정렬된 배열이 필요합니다)
arr.sort()

# 찾을 숫자 입력 받기
x = int(input("찾을 숫자를 입력하세요: "))

# 이진 탐색 수행
result = binary_search(arr, x)

# 결과 출력
if result != -1:
    print(f"{x}은 배열의 {result}번째 인덱스에 있습니다.")
else:
    print(f"{x}는 배열에 존재하지 않습니다.")

print('------------------------')

# 팩토리얼

def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n-1)

n = int(input("숫자 입력 : "))
print(f"{n}의 팩토리얼은 {factorial(n)}")

  