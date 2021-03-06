def get_valid_input(input_string, valid_options):
    """
    Function to get valid input from user.
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response
