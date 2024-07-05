player = {
  'name' : 'names',
  'age' : 12,
  'alive' : True,
  'food' : [' �','�'],
  'friends' : {
    'name' : 'lloiy',
    'food' :['�']
  }
}

player.pop('age') # 삭제
player['xp'] = 125 # 추가
player['food'].append('�')
print(player)

player['food'] = '�'
player.pop('alive')
print(player)