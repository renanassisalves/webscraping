class Team:
    def __init__(self, teamName, year, wins, losses, otLosses,
                 winPercentage, goalsFor, goalsAgainst, goalsDifference):
        self.teamName = teamName
        self.year = year
        self.wins = wins
        self.losses = losses
        self.otLosses = otLosses
        self.winPercentage = winPercentage
        self.goalsFor = goalsFor
        self.goalsAgainst = goalsAgainst
        self.goalsDifference = goalsDifference

    def __str__(self):
        return (
                f"\n\nTeam name: {self.teamName}\n"
                f"Year: {self.year}\n"
                f"Wins: {self.wins}\n"
                f"Losses: {self.losses}\n"
                f"OT Losses: {self.otLosses}\n"
                f"Win Percentage: {self.winPercentage}\n"
                f"Goals For: {self.goalsFor}\n"
                f"Goals Against: {self.goalsAgainst}\n"
                f"Goals difference: {self.goalsDifference}\n\n"
                )