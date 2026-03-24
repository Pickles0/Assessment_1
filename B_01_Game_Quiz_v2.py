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

Press <enter> it you want to play infinite mode.

Press <xxx> if you want to quit during the quiz.

Good luck.

    """)

# checks for an integer with optional upper
# lower limits and an optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    #integer (ie: rounds / "high number"
    elif low is not None and high is None:
        error = ("Please enter an integer this "
                 f"more than / equal to {low}")

    # id the number needs to between low and high
    else:
        error = ("Please enter an integer that"
                 f" is between {low} and {high}")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check the integer is not too high...
            elif high is not None and response > high:
                print(error)

            # if the response is valid, return it
            else:
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
print()

# Display the instructions if the user want to see them
if want_instructions == "yes":
    instructions()

# Ask for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ",
                       low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite Mode)♾️♾️♾️"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)

# find the equation
    # first random number
    number_1 = random.randint(0, 10)
    # find the symbol to connect the numbers
    symbol_list = ["+", "-", "*"]
    # find the second random number
    number_2 = random.randint(0, 10)
    # use the random connector
    symbol = random.choice(symbol_list)

    # Create the connector
    if symbol == "+":
        answer = number_1 + number_2
    elif symbol == "*":
        answer = number_1 * number_2
    else:
        answer = number_1 - number_2

    # Put the question together
    user_answer = int_check(f"{number_1} {symbol} {number_2} = ", exit_code= "xxx")

    # check that they don't want to  quit
    if user_answer == "xxx":
        # set end_game to use so that outer loop can be broken
        end_game = "yes"
        break

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

    rounds_played += 1

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