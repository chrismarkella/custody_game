# YouTube: https://www.youtube.com/watch?v=aMy3dYt5itE&t=748s 12:31

import axelrod as axl

player1 = axl.Cooperator()
player2 = axl.Defector()
player3 = axl.TitForTat()

match = axl.Match([player1, player2], 5)
print(f'playing the match: {match.play()}')
print(f'final score: {match.final_score()}')
