#  Jacob Milham
#  CIS 267
#  Spring 2026
import menu
from models.batch import Batch
from models.company import Company
from models.record import Record
from models.user import User


def open_company():
    print("O:open_company")
    # this is temporary. Until the proper functionality is added
    return True


def create_batch():
    print("create batch")
    name = input("File name")
    date = input("date")
    temp = Batch(name, date)
    return temp


def pick_batch():
    print("P:pick batch")


def save_company():
    print("S:save company")


def new_company() -> Company:
    print("New company")
    name = input("Company name:")
    description = input("Company Description:")
    if input("Is the company active").lower() in ["yes", "true"]:
        active = True
    else:
        active = False
    temp = Company(name, description, active)
    return temp


def manage_users():
    print("M:manage users")


def exit(unsaved_data: bool) -> bool:
    if unsaved_data:
        print("unsaved data")
        return False
    else:
        return True


quit = False
unsaved_data = False
current_company = None
while not quit:
    selection = menu.recieve_input()
    if menu.valid(selection):
        if selection == "O":
            current_company = open_company()
        elif selection == "C":
            create_batch()
        elif selection == "P":
            pick_batch()
        elif selection == "S":
            save_company()
        elif selection == "N":
            current_company = new_company()
        elif selection == "E":
            quit = exit(unsaved_data)
        elif selection == "M":
            if current_company == None:
                print("No company currently is selected")
            else:
                manage_users()
