#  Jacob Milham
#  CIS 267
#  Spring 2026
options = ["O", "C", "P", "S", "N", "E", "M"]


def recieve_input() -> str:
    return input(":").upper()


def valid(input_to_validate: str) -> bool:
    if input_to_validate in options:
        return True
    else:
        print("Not a valid option!")
        return False
