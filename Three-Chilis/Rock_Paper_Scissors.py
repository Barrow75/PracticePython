# Prompt: Make a two-player Rock-Paper-Scissors game.

# make a welcome message
print("Welcome to Rock Paper Scissors")


# main funtion that runs the game
def main():
    score1 = 0
    score2 = 0


    while True:
        player_1 = input("Player 1: Rock, Paper, or Scissors?: ")
        player_2 = input("Player 2: Rock, Paper, or Scissors?: ")

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
main()
