
class Player:
    player_stats = {}

    def __init__(self, stats):
        self.player_stats = {**stats}
        self.player_name = stats["player_name"]
        self.age = stats["age"]
        self.games = stats["games"]
        self.games_started = stats["games_started"]
        self.minutes_played = stats["minutes_played"]
        self.field_goals = stats["field_goals"]
        self.field_attempts = stats["field_attempts"]
        self.field_percent = stats["field_percent"]
        self.three_fg = stats["three_fg"]
        self.three_attempts = stats["three_attempts"]
        self.three_percent = stats["three_percent"]
        self.two_fg = stats["two_fg"]
        self.two_attempts = stats["two_attempts"]
        self.two_percent = stats["two_percent"]
        self.effect_fg_percent = stats["effect_fg_percent"]
        self.ft = stats["ft"]
        self.fta = stats["fta"]
        self.ft_percent = stats["ft_percent"]
        self.ORB = stats["ORB"]
        self.DRB = stats["DRB"]
        self.TRB = stats["TRB"]
        self.AST = stats["AST"]
        self.STL = stats["STL"]
        self.BLK = stats["BLK"]
        self.TOV = stats["TOV"]
        self.PF = stats["PF"]
        self.PTS = stats["PTS"]
        self.team = stats["team"]
        self.season = stats["season"]

    def print_all_stats(player):
        print("Player Name:", player.player_name)
        print("Age:", player.age)
        print("Games:", player.games)
        print("Games Started:", player.games_started)
        print("Minutes Played:", player.minutes_played)
        print("Field Goals:", player.field_goals)
        print("Field Attempts:", player.field_attempts)
        print("Field Percentage:", player.field_percent)
        print("Three-Point FG:", player.three_fg)
        print("Three-Point Attempts:", player.three_attempts)
        print("Three-Point Percentage:", player.three_percent)
        print("Two-Point FG:", player.two_fg)
        print("Two-Point Attempts:", player.two_attempts)
        print("Two-Point Percentage:", player.two_percent)
        print("Effective FG Percentage:", player.effect_fg_percent)
        print("Free Throws:", player.ft)
        print("Free Throw Attempts:", player.fta)
        print("Free Throw Percentage:", player.ft_percent)
        print("Offensive Rebounds:", player.ORB)
        print("Defensive Rebounds:", player.DRB)
        print("Total Rebounds:", player.TRB)
        print("Assists:", player.AST)
        print("Steals:", player.STL)
        print("Blocks:", player.BLK)
        print("Turnovers:", player.TOV)
        print("Personal Fouls:", player.PF)
        print("Points:", player.PTS)
        print("Team:", player.team)
        print("Season:", player.season)

    def print_basic_stats(player):
        print("Player Name:", player.player_name)
        print("Age:", player.age)
        print("Games:", player.games)
        print("Minutes Played:", player.minutes_played)
        print("Field Goals:", player.field_goals)
        print("Field Percentage:", player.field_percent)
        print("Three-Point FG:", player.three_fg)
        print("Three-Point Percentage:", player.three_percent)
        print("Two-Point FG:", player.two_fg)
        print("Two-Point Percentage:", player.two_percent)
        print("Effective FG Percentage:", player.effect_fg_percent)
        print("Free Throws:", player.ft)
        print("Free Throw Percentage:", player.ft_percent)
        print("Total Rebounds:", player.TRB)
        print("Assists:", player.AST)
        print("Steals:", player.STL)
        print("Blocks:", player.BLK)
        print("Turnovers:", player.TOV)
        print("Personal Fouls:", player.PF)
        print("Points:", player.PTS)
        print("Team:", player.team)
        print("Season:", player.season)