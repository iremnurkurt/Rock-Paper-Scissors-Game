import random

def play_game():
    print("Welcome to the Rock Paper Scissors game!")
    print("Please make your selection: ")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    choices = ["Rock", "Paper", "Scissors"]
    player_choice = int(input("Please make your selection (1-3): "))
    computer_choice = random.randint(1, 3)

    print("You: " + choices[player_choice - 1])
    print("Computer: " + choices[computer_choice - 1])

    if player_choice == computer_choice:
        print("Draw!")
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        print("Congratulations you won!")
    else:
        print("Unfortunately you lost.")

while True:
    play_game()
    play_again = input("Do you want to play again? (Y/N) ")
    if play_again.upper() != "Y":
        break

print("Game over. Have a nice day!")
