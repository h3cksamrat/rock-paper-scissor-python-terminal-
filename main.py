from random import randint

# instruction
print("Instructions to follow:",
      "1. Enter the numeric value for your choice.",
      "1 for rock",
      "2 for paper",
      "3 for scissors",
      "Enter q to exit", sep="\n")

choices = ["ROCK", "PAPER", "SCISSOR"]

while True:
    user_choice = input("rock, paper or scissor >>> ")
    if user_choice.lower() == "q":
        break
    user_choice = int(user_choice)
    computer_choice = randint(1, 3)
    print(choices[user_choice - 1], "Vs.", choices[computer_choice - 1], ">>> ", end="")

    if (user_choice - computer_choice) == 1 or (user_choice - computer_choice) == -2:
        print("You win\n")
    elif user_choice == computer_choice:
        print("Tie\n")
    else:
        print("You loose\n")
