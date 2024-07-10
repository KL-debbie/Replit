apart = [['101호','102호'], ['201호','202호'], ['301호','302호']]

stock = [["시가",100,200,300], ["종가",80,210,330]]

stock = {"시가":[100,200,300], "종가":[80,210,330]}

stock = {"10/10":[80,110,70,90], "10/11":[210,230,190,200]}

apart = [ [101, 102], [201, 202], [301, 302] ]
for a in apart:
  for aa in a:
    print(aa,'호')
    #print('-----')
  #print('-----')
print('-----')

for a in apart[::-1]:
  for aa in a:
    print(aa,'호')

for a in apart[::-1]:
  for aa in a[::-1]:
    print(aa,'호')

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []
for a in data:
  bin = []
  for b in a:
    bin.append(b * 1.0014)
  result.append(bin)
  #print('------------')
print(result)


ohlc = [["open", "high", "low", "close"],
  [100, 110, 70, 100],
  [200, 210, 180, 190],
  [300, 310, 300, 310]]

for a in ohlc[1:]:
  if (a[3] > 150):
    print(a[3])

for a in ohlc[1:]:
  if (a[3] >= a[0]):
    print(a[3])

volatility = []
for a in ohlc[1:]:
  volatility.append(a[1] - a[2])
print(volatility)

for a in ohlc[1:]:
  if a[3] > a[0]:
    print(a[1] - a[2])

profit =0
for a in ohlc[1:]:
  profit += a[0]-a[3]
print(profit)