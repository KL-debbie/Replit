class Player:

  def __init__(self, team, record):
    self.team = team
    self.xp = 1500
    self.record = record


  def introduce(self):
    print(f"Hello! I like {self.team} and it's in {self.record}")

class Team:
  def __init__(self, team_name):
    self.team_name = team_name
    self.players= []

  def show_players(self):
    for player in self.players:
      player.introduce()

  def add_player(self, name):
    new_player = Player(name, self.team_name)
    self.players.append(new_player)

player = Player(team="doo", record=3)
player2 = Player(team="kio", record=8)

team_x = Team('Team_d')
'''team_x = Team(3)'''
team_x.add_player('km')

team_y = Team('Team_k')
team_y.add_player('jh')

team_x.show_players()
team_y.show_players()

  