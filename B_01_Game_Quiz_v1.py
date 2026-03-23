import math
import random
# checks users enter yes(y) or no (n)
def yes_no(question):

    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        if response == "yes" or response == "y":
                return "yes"
        elif response == "no" or response == "n":
                return "no"
        else:
                print("Please enter yes/no")

# print instructions
def instructions():
    """Prints instructions"""


    print("""
*** Instructions ***

In this quiz you will be subjected to multiple math 
questions. Your goal is to answer as many questions as 
possible correctly. 

Good luck.

    """)

# checks for an integer with optional upper
# lower limits and an optional exit code for infinite mode
# / quitting the game
def int_check(question):
    while True:
        error = "Please enter an Integer"

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)


            return response
        except ValueError:
            print(error)

#Main Routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = []
rounds_won = 0
rounds_lost = 0
game_history = []
all_scores = []

# introduce the player to the game
print("Welcome to the Math Quiz!")
print()

# ask if they want to see the instructions
want_instructions = yes_no("do you want to see the instructions? ")

# Display the instructions if the user want to see them
if want_instructions == "yes":
    instructions()


rounds_heading = f"\n💿💿💿 Round {rounds_played + 1}💿💿💿"

print(rounds_heading)

while True:
    # first random number
    secret_number_1 = random.randint(0, 10)
    # find the symbol to connect the numbers
    secret_symbol_list = ["+", "-", "*"]
    # find the second random number
    secret_number_2 = random.randint(0, 10)
    # use the random connector
    secret_symbol = random.choice(secret_symbol_list)

    # Create the connector
    if secret_symbol == "+":
        answer = secret_number_1 + secret_number_2
    elif secret_symbol == "*":
        answer = secret_number_1 * secret_number_2
    else:
        answer = secret_number_1 - secret_number_2

    # Put the question together
    user_answer = int_check(f"{secret_number_1} {secret_symbol} {secret_number_2} = ")

    # If the user answers with enter treat it as nothing
    if user_answer == "infinite":
        user_answer = 0
    # Check if the got it right
    if user_answer == answer:
        feedback = "You got it correct!"
        rounds_won += 1
    else:
        feedback = "You got it wrong"
        rounds_lost += 1

    history_feedback = f"Round {rounds_played}: {feedback}"

    game_history.append(history_feedback)

    print(feedback)
    print()

    # ask if they want to stop
    want_to_exit = yes_no("Do you want to stop?")
    print()


    rounds_played += 1

    # if they want to stop then break
    if want_to_exit == "yes":
        end_game = "yes"
    else:
        continue

    if end_game == "yes":
        break


#calculate statistics
percent_won = rounds_won / rounds_played * 100
percent_lost = rounds_lost / rounds_played * 100

#Output game statistics
print("📊📊📊 Game Statistics 📊📊📊")
print(f"👍 Percent won: {percent_won:.2f} \t "
        f"😢 Percent lost: {percent_lost:.2f} \t "
        f"👍 Won: {rounds_won} \t"
        f"😢 Lost: {rounds_lost} \t")

# ask user if they want to see their game history and output if requested
see_history = yes_no("\nDo you want to see your game history?")
if see_history == "yes":
    for item in game_history:
        print(item)

print()
print("Thanks for playing.")