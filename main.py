import random


def get_user_input () :
    while True :
        user_input = input("Enter your choice rock/paper/scissor: ")
        if user_input == "rock" or user_input == "scissor" or user_input == "paper" :
            user_input = user_input.capitalize()
            break
        else :
            print("Invalid details!!Enter again..")
    return user_input


def get_computer_choice () :
    random_number = random.randint(1, 3)
    selections = {1 : "Rock", 2 : "Scissor", 3 : "Paper"}
    computer_choice = selections[random_number]
    return computer_choice


def get_winner (user_input, computer_choice) :
    # if user_input == "Rock" or user_input == "Scissor" or user_input=="Paper":
    if user_input == computer_choice :
        return "Draw!"
    elif user_input == "Rock" and computer_choice == "Scissor" :
        return "You won!***Rock crushed Scissor***"
    elif user_input == "Scissor" and computer_choice == "Paper" :
        return "You won!***Scissor cuts Paper***"
    elif user_input == "Paper" and computer_choice == "Rock" :
        return "You won!***Paper wrapped Rock***"
    else :
        return "You lose!***Better Luck Next Time...***"


# else:
# return "Please, enter valid details!"

user_selection = get_user_input()
computer_selection = get_computer_choice()
print(f"Yours selection is {user_selection}")
print(f"Computer\'s selection is {computer_selection}")
winner = get_winner(user_selection, computer_selection)
print(winner)

