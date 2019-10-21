import axelrod as axl

player1 = axl.Cooperator()
player2 = axl.Defector()
player3 = axl.TitForTat()

match = axl.Match([player1, player2], 5)
match.play()
print(f'final score: {match.final_score()}')
