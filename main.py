from registration import register
from login import login_menu

def main_menu():
    while True:
        print("-------- Main Menu ----------")

        choice = int(input("""
        1: Register
        2- LogIn
        3- Exit
        
        Your Choice: """))

        if choice == 1:
            register()
        elif choice == 2:
           login_menu()

        elif choice == 3:
            exit()


print("######## CROWD FUNDING ############")
main_menu()