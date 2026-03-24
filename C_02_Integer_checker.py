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