#  Jacob Milham
#  CIS 267
#  Spring 2026
import menu
from models import batch
from models import company
# from models import record
from models import user


def open_company():
    print("O:open_company")
    # this is temporary. Until the proper functionality is added
    return True


def create_batch():
    print("create batch")
    name = input("File name")
    date = input("date")
    temp = batch.Batch(name, date)
    return temp


def pick_batch():
    print("P:pick batch")


def save_company():
    print("S:save company")


def new_company() -> company.Company:
    print("New company")
    name = input("Company name:")
    description = input("Company Description:")
    if input("Is the company active").lower() in ["yes", "true"]:
        active = True
    else:
        active = False
    temp = company.Company(name, description, active)
    return temp


def manage_users():
    print("N:New User")
    print("M:Modify User")
    print("D:Delete User")
    print("E:Exit")

    quit = False
    while not quit:
        selection = menu.recieve_input()
        if selection == "N":
            print("Enter user type. User, Admin, Auditor")
            selection = menu.recieve_input()
            if selection == "USER":
                return user.User()
            elif selection == "ADMIN":
                return user.Admin()
            elif selection == "AUDITOR":
                return user.Auditor()
            else:
                print("Unavailable option")
        elif selection == "M":
            pass
        elif selection == "D":
            pass
        elif selection == "E":
            quit = True


def exit(unsaved_data: bool) -> bool:
    if unsaved_data:
        print("unsaved data")
        return False
    else:
        return True


quit = False
unsaved_data = False
current_company = None

print("The current available options are:")
for option in menu.options:
    print(option, end=", ")

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
            if current_company is None:
                print("No company currently is selected")
            else:
                print(manage_users())
