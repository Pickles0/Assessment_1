import random
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

# find the question
while True:
    #first random number
    secret_number_1 = random.randint(0, 10)
    #find the symbol to connect the numbers
    secret_connector_list = ["+","-","*"]
    #find the second random number
    secret_number_2 = random.randint(0,10)
    #use the random connector
    secret_connector = random.choice(secret_connector_list)

    # Create the connector
    if secret_connector == "+":
        answer = secret_number_1 + secret_number_2
    elif secret_connector == "*":
        answer = secret_number_1 * secret_number_2
    else:
        answer = secret_number_1 - secret_number_2

    # Put the question together
    user_answer = int_check(f"{secret_number_1} {secret_connector} {secret_number_2} = ")

    # Check if the got it right
    if user_answer == answer:
        print("You got it correct!")
    else:
        print("You lost")

    # ask if they want to stop
    want_to_exit = yes_no("Do you want to stop?")

    # if they want to stop then break
    if want_to_exit == "yes":
        break
    else:
        continue



    
