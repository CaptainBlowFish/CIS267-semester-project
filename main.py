#  Jacob Milham
#  CIS 267
import menu


def open_company():
    print("O:open_company")


def create_batch():
    print("C:create batch")


def pick_batch():
    print("P:pick batch")


def save_company():
    print("S:save company")


def new_company():
    print("N:new company")


def exit(unsaved_data: bool) -> bool:
    if unsaved_data:
        print("unsaved data")
        return False
    else:
        return True


quit = False
unsaved_data = False
while not quit:
    selection = menu.recieve_input()
    if menu.valid(selection):
        if selection == "O":
            open_company()
        elif selection == "C":
            create_batch()
        elif selection == "P":
            pick_batch()
        elif selection == "S":
            save_company()
        elif selection == "N":
            new_company()
        elif selection == "E":
            quit = exit(unsaved_data)
