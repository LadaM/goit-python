from constants import * # imports all attributes from the file constants.py

# type annotation for better usability of the code in any IDEE
def minutes_to_seconds(minutes: int) -> str:
    res: int = minutes * SECONDS_IN_MINUTE
    return f"{minutes} min in seconds is: {res}"

def minutes_to_milliseconds(minutes: int) -> str:
    res: int = minutes * SECONDS_IN_MINUTE * MILLISECONDS_IN_SECOND
    return f"{minutes} min in milliseconds is {res}"


# the code below will only be executed when this file is executed, not when it's imported
if __name__ == "__main__":
    """ entrypoint to the file. Can show how the functions are used or for testing
    """
    print(minutes_to_seconds(10))