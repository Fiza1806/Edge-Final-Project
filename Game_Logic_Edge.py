#Rock Paper and Scissors Sample Game Logic by Fiza and Adel

print("Welcome to Rock, Paper and Scissors!A game for two! Please enter your name.\n")

player1 = input("Player 1 name:")
player2 = input("Player 2 name:")
player1_answer = input(str(player1) + " do yo want to choose rock, paper or scissors?")
player2_answer = input(str(player2) + " do you want to choose rock, paper or scissors?")

def compare_choice(p1, p2):
    if p1 == p2:
        return("It's a draw!")
    elif p1 == 'rock':
        if p2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif p1 == 'scissors':
        if p2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif p1 == 'paper':
        if p2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("OH NO! You have not entered rock, paper or scissors,please try again.")


print(compare_choice(player1_answer, player2_answer))
