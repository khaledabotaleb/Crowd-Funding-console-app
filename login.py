import json
from create_project import create_project
from delete import delete_project
from edit_project import edit_project
from search import search_project
from view_projects import view_projects


def get_user(email, password):
    list_users = []
    json_file = open('users_data.json')
    for line in json_file:
        Dict = json.loads(line)
        list_users.append(Dict)

    for dict in list_users:
        if email == dict['Email'] and password == dict['Password']:
            return email
        else:
            pass


def login():
    email = input("Email: ")
    password = input("Password: ")
    user = get_user(email, password)
    if user:
        print("Login Succeeded!")
        return email
    else:
        print("Login Failed!")
        return 0


def login_menu():
    print("--------------- Log-In --------------------")
    user_mail = login()
    if user_mail:
        while True:
            choice = int(input("""
                1- Create new project
                2- View all projects
                3- Edit project
                4- Delete project
                5- Search for a project
                6- Exit
                """))

            if choice == 1:
                print("create project")
                create_project(user_mail)
            elif choice == 2:
                # print("view projects")
                view_projects(user_mail)
            elif choice == 3:
                print("edit project")
                edit_project(user_mail)
            elif choice == 4:
                print("delete project")
                delete_project(user_mail)
            elif choice == 5:
                search_project(user_mail)
            elif choice == 6:
                return 0