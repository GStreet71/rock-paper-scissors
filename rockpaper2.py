from getpass import getpass
from colorama import Fore, Back, Style

def selections(name1, name2, round):
    print(Fore.GREEN + f"Round {round}\n")
    print("Select your move (R, P or S)\n" + Style.RESET_ALL)
    player1 = getpass(f"{name1} > ").upper()
    player2 = getpass(f"{name2} > ").upper()
    return player1, player2

def play(name1, name2, player1, player2, round, score1, score2):
    if player1 == "R":
        if player2 == "P":
            print(Fore.MAGENTA + Back.GREEN + f"\n{name1}'s Rock is smothered by {name2}'s Paper!" + Style.RESET_ALL)
            score2 += 1
            round += 1
            return name1, name2, player1, player2, round, score1, score2
        elif player2 == "R":
            print(Fore.MAGENTA + Back.GREEN + f"\nYou both picked the same thing. Retry" + Style.RESET_ALL)
            selections(name1, name2)
        else:
            score1 += 1
            round += 1
            print(Fore.MAGENTA + Back.GREEN + f"\n{name2}'s Scissors was smashed to bits by {name1}'s Rock!" + Style.RESET_ALL)
            return score1, score2
    elif player1 == "P":
        if player2 == "R":
            score1 += 1
            round += 1
            print(Fore.MAGENTA + Back.GREEN + f"\n{name2}'s Rock is smothered by {name1}'s Paper!" + Style.RESET_ALL)
            return score1, score2
        elif player2 == "P":
            print(Fore.MAGENTA + Back.GREEN + f"\nYou both picked the same thing. Retry" + Style.RESET_ALL)
            selections()
        else:
            score2 += 1
            round += 1
            print(Fore.MAGENTA + Back.GREEN + f"\n{name1}'s Paper was cut to shreds by {name2}'s Scissors!" + Style.RESET_ALL)
            return score1, score2
    else:
        if player2 == "R":
            score2 += 1
            round += 1
            print(Fore.MAGENTA + Back.GREEN + f"\n{name1}'s Scissors was smashed to bits by {name2}'s Rock!" + Style.RESET_ALL)
            return name1, name2, player1, player2, round, score1, score2
        elif player2 == "S":
            print(Fore.MAGENTA + Back.GREEN + f"\nYou both picked the same thing. Retry" + Style.RESET_ALL)
            selections()
        else:
            score1 += 1
            round += 1
            print(Fore.MAGENTA + Back.GREEN + f"\n{name2}'s Paper was cut to shreds by {name1}'s Scissors!" + Style.RESET_ALL)
            return name1, name2, player1, player2, round, score1, score2

def main(name1, name2, player1, player2, round, score1, score2):
    while round <= 3: #Odd number of rounds
        selections(name1, name2, round)
        play(name1, name2, player1, player2, round, score1, score2)
        round += 1

    if score1 > score2 :
        print(Fore.CYAN + f"{name1} wins with 2 victories!")
    else:
        print(Fore.MAGENTA + f"{name2} wins with 2 victories!")

print(Fore.MAGENTA + " E P I C     " + Fore.MAGENTA + Back.GREEN + "ROCK," + Fore.CYAN + " PAPER," + Fore.RED + " SCISSORS" + Style.RESET_ALL + Fore.MAGENTA +  "    B A T T L E\n")
name1 = input(Fore.CYAN + "Welcome Player 1. Enter your name: ").capitalize()
name2 = input("Welcome Player 2. Enter your name: ").capitalize()
round = 1
score1 = 0
score2 = 0
player1 = ""
player2 = ""


main(name1, name2, player1, player2, round, score1, score2)


