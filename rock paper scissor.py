import random

wins_computer = 0
wins_user = 0

Options = ["rock", "paper", "scissors"]

while True:
    users_input = input("Type rock/paper/scissors or Q to quit: ").lower()
    if users_input == "q":
        break
    if users_input not in Options:
        continue
    random_number = random.randint(0, 2)
    # rock:0, paper:1, scissors:2
    computer_choose = Options[random_number]
    print("Computer choose", computer_choose + ".")

    if users_input == "rock" and computer_choose == "paper":
        print("WINNER!!")
        wins_user += 1
    elif users_input == "scissors" and computer_choose == "paper":
        print("WINNER!!")
        wins_user += 1

    elif users_input == "paper" and computer_choose == "rock":
        print("WINNER!!")
        wins_user += 1

    elif users_input == "scissors" and computer_choose == "scissors":
        print("TIE ʕ•́ᴥ•̀ʔっ")
        wins_user += 0

    elif users_input == "paper" and computer_choose == "paper":
        print("TIE ʕ•́ᴥ•̀ʔっ")
        wins_user += 0

    elif users_input == "rock" and computer_choose == "rock":
        print("TIE ʕ•́ᴥ•̀ʔっ")
        wins_user += 0


    else:
        print("you loose :( ")
        wins_computer += 1

print("You won", wins_user, "times.")
print("The computer won", wins_computer, "times.")
print("Goodbye👋≧◉ᴥ◉≦ :) ")
