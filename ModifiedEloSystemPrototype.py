from math import exp

# This function computes the multiplier to account for the difference in Elo of the two players.
# ComputeMuE: (delta_E::Integer) -> (Float)
def ComputeMuE(deltaE):
     return (1/(1+exp(0.003*deltaE)))

# This function computes the multiplier to account for the score of the game.
# ComputeMuDeltaS: (delta_S::Integer) -> (Float) 
def ComputeMuDeltaS(delta_S):
    # This defines the "win by 2 points" nature of many games, but this constant can be changed.
    delta_S_min = 2
    # This defines the maximum difference between score at the end of a match.
    delta_S_T = 11
    return abs((-0.9 / delta_S_min) * (delta_S_T - delta_S) + 1)


# This function computes the new Elo Rating of each player that results from the game.
# ComputeNewElo: (e_A::Integer, S_A::Integer, e_B::Integer, S_B::Integer, winner::Boolean) -> (Integer, Integer)
def ComputeNewElo(e_A, S_A, e_B, S_B, winner):
    delta_E = e_A - e_B
    delta_S = abs((S_A - S_B))
#    print("delta_E = " + str(delta_E))
    if winner == True:
        delta_E = delta_E * -1
    mu_E = ComputeMuE(delta_E)
#    print("mu_E = " + str(mu_E))
    mu_delta_S = ComputeMuDeltaS(delta_S)
#    print("mu_delta_S = " + str(mu_delta_S))
    if winner == False:
        e_A = e_A + (0.1 * e_A * mu_E * mu_delta_S)
        e_B = e_B - (0.1 * e_B * mu_E * mu_delta_S)
    if winner == True:
        e_A = e_A - (0.1 * e_A * mu_E * mu_delta_S)
        e_B = e_B + (0.1 * e_B * mu_E * mu_delta_S)
    return [e_A, e_B]

player1E = 750
player1S = 5
player2E = 900
player2S = 11
winner = True

newElos = ComputeNewElo(player1E, player1S, player2E, player2S, winner)
newElos[0] = round(newElos[0])
newElos[1] = round(newElos[1])

print("\n" + "Player 1's starting Elo rating: " + str(player1E))
print("Player 2's starting Elo rating: " + str(player2E))

print("\n" + "Score: Player 1 (" + str(player1S) + ") vs. Player 2 (" + str(player2S) + ")")

print("\n" + "Player 1's new Elo rating: " + str(newElos[0]))
print("Player 2's new Elo rating: " + str(newElos[1]))

print("\n" + "Change in Player 1's Elo rating: " + str(newElos[0]-player1E))
print("Change in Player 2's Elo rating: " + str(newElos[1]-player2E))
