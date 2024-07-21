def get_total_page(m,n):  # m = 게시물 총 개수, n = 한 페이지에 보여줄 게시물 수
  if m % n == 0:
    return m // n
  else:
    return m // n + 1    # // 몫

# 총 페이지 수 = m / n + 1
print(get_total_page(5,10))
print(get_total_page(15,10))
print(get_total_page(25,10))
print(get_total_page(30,10))
