from requests import get

websites = ('google.com', 'https://twitter.com', 'facebook.com', 'naver.com',
            'daum.net')

results = {}

for x in websites:
  if not x.startswith('https://'):
    x = f"https://{x}"
  response = get(x)
  if response.status_code == 200:
    results[x] = 'ok'
  else:
    results[x] = 'failed'

print(results)
