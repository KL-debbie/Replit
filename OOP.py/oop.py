class Player:

  def __init__(self, name, team):
    self.name = name
    self.xp = 1500
    self.team = team

  def introduce(self):
    print(f"Hello I'm {self.name} And I play for {self.team}")


class Team:

  def __init__(self, team_name):
    self.team_name = team_name
    self.players = []

  def show_players(self):
    for player in self.players:
      player.introduce()

  def add_player(self, name):
    new_player = Player(name, self.team_name)
    self.players.append(new_player)


player = Player(name="player", team='Team X')

player2 = Player(name='player2', team='Team Y')

team_x = Team('Team_X')

team_x.add_player("helllow")

team_y = Team("Team_Y")

team_y.add_player("lyynbmn")

team_x.show_players()
team_y.show_players()
