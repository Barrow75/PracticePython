# Prompt: Make a two-player Rock-Paper-Scissors game.

# make a welcome message
print("Welcome to Rock Paper Scissors")


# main funtion that runs the game

'''def main():
    score1 = 0
    score2 = 0


    while True:
        player_1 = input("Player 1: Rock, Paper, or Scissors?: ").capitalize()
        player_2 = input("Player 2: Rock, Paper, or Scissors?: ").capitalize()

        if player_1 == 'Rock' and player_2 == 'Scissors':
            print("Player 1 Wins: Rock beats scissors")
            score1 += 1
            print("Player 1 Score:", score1)
            print("Player 2 Score:", score2)

        elif player_2 == 'Rock' and player_1 == 'Scissors':
            print("Player 2 Wins: Rock beats scissors")
            score2 += 1
            print("Player 2 Score:", score2)
            print("Player 1 Score:", score1)

        elif player_1 == 'Scissors' and player_2 == 'Paper':
            print("Player 1 Wins: Scissors beats Paper")
            score1 += 1
            print("Player 1 Score:", score1)
            print("Player 2 Score:", score2)

        elif player_1 == 'Paper' and player_2 == 'Scissors':
            print("Player 2 Wins: Scissors beats Paper")
            score2 += 1
            print("Player 2 Score:", score2)
            print("Player 1 Score:", score1)

        elif player_1 == 'Paper' and player_2 == 'Rock':
            print("Player 1 Wins: Paper beats Rock")
            score1 += 1
            print("Player 1 Score:", score1)
            print("Player 2 Score:", score2)

        elif player_1 == 'Rock' and player_2 == 'Paper':
            print("Player 2 Wins: Paper beats Rock")
            score2 += 1
            print("Player 2 Score:", score2)
            print("Player 1 Score:", score1)

        elif player_1 == 'Rock' and player_2 == 'Rock':
            print("Tie go agian")
        elif player_1 == 'Paper' and player_2 == 'Paper':
            print("Tie go agian")
        elif player_1 == 'Scissors' and player_2 == 'Scissors':
            print("Tie go agian")

        if score1 == 3:
            print("Player 1 wins")
            break
        elif score2 == 3:
            print("Player 2 wins")
            break
main()'''

# refactor the code to avoid long if and else statements
def main():
    # keep track of the score for both players
    score1 = 0
    score2 = 0

    # win conditions using dictionary
    win_conditions = {
        "Rock": "Scissors",
        "Scissors": "Paper",
        "Paper" : "Rock"
    }

    while True:
        # prompt players
        player1 = input("Player 1: Rock, Paper, or Scissors: ").capitalize()
        player2 = input("Player 2: Rock, Paper, or Scissors: ").capitalize()

        # check for a tie
        if player1 == player2:
            print("Tie; Go again!!")
            continue

        # check if player 1 wins
        if win_conditions.get(player1) == player2:
            print(f"Player 1 Wins: {player1}")
            score1 += 1

        # check if player 2 wins
        elif win_conditions.get(player2) == player1:
            print(f"Player 2 Wins: {player2}")
            score2 += 1

        else:
            print("Inalid input; Options are Rock, Paper or Scissors")
            continue

        # print the final score
        print(f"Player 1: {score1} | Player 2: {score2}\n")

        if score1 == 3:
            print("Player 1 wins")
            break
        elif score2 == 3:
            print("Player 2 wins")
            break

main()
