import json
from create_project import validate_datetime
from view_projects import view_projects


def search_project(user_mail):
    view_projects(user_mail)

    project_date = input('\nWrite project date (dd/mm/yyyy) : ')
    try:
        valid_date = validate_datetime(project_date)
        if valid_date:
            list = []
            json_file = open('projects_data.json')
            for line in json_file:
                Dict = json.loads(line)
                list.append(Dict)

            # search for poject
            for dict in list:

                if project_date == dict['Start_Time'] or project_date == dict['End_Time']:
                    print("\nYour project information:")
                    print(dict)
                else:
                    print("this project is n't exist ,, please try again")
                    search_project(user_mail)

        else:
            print("\nYour data is invalid ,, please enter valid data :")

    except ValueError:
        print('Invalid date!')