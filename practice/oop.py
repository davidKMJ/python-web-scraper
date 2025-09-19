class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team

    def introduce(self):
        print(f"Hello! I'm {self.name} and I play for {self.team}.")


class SpecialPlayer(Player):
    def __init__(self, name, team):
        super().__init__(name, team)
        self.xp = 3000

    def shout(self):
        print("I'm special!")


class Team:
    def __init__(self, team_name, *args):
        self.team_name = team_name
        self.players = list(args)

    def __str__(self):
        return f"{self.team_name} has {len(self.players)} player{'' if len(self.players)==1 else 's'}."

    def introduce_players(self):
        for player in self.players:
            player.introduce()

    def add_player(self, player):
        self.players.append(player)

    def add_player_by_name(self, name):
        player = Player(name, self.team_name)
        self.players.append(player)


first_player = Player("John", "Red")
second_player = Player("Alice", "Blue")

first_player.introduce()
second_player.introduce()

team_red = Team("Red", first_player)
team_blue = Team("Blue", second_player)
team_red.add_player_by_name("Mike")

third_player = SpecialPlayer("Bob", "Red")
team_red.add_player(third_player)

print(team_red)
print(team_blue)

team_red.introduce_players()
team_blue.introduce_players()
