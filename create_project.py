import datetime
import json


def validate_datetime(input_date):
    try:
        day, month, year = input_date.split('/')
        valid_date = True
        print(day, month, year)
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        valid_date = False

    if valid_date:
        return input_date
    else:
        print("In-valid date!")
        return 0


def validate_project(user_mail):
    title = input("Project Title: ")
    if title:
        list = []
        json_file = open('projects_data.json')
        for line in json_file:
            Dict = json.loads(line)
            if Dict['User'] == user_mail:
                list.append(Dict)
        for dict in list:
            if title == dict['Title'] and dict['User'] == user_mail:
                print("\nthis project name is already exit ,, please try again")
                create_project(user_mail)
        details = input("Project Details: ")
        total_target = input("Total Target: ")
        if total_target:
            start_date = validate_datetime(input("Start Time (dd/mm/yy): "))
            if start_date:
                end_date = validate_datetime(input("End Time (dd/mm/yy): "))
                if end_date:
                    project = {
                        "Title": title,
                        "Details": details,
                        "Total_Target": total_target,
                        "Start_Time": start_date,
                        "End_Time": end_date,
                        "User": user_mail}
                    return project
    else:
        print("Title can not be empty!")
    return False


def save_project(project_data):
    projects = open("projects_data.json", "a")
    json.dump(project_data, projects)
    projects.write("\n")
    projects.close()
    print("Project Created!")


def create_project(user_mail):
    project = validate_project(user_mail)

    if project:
        save_project(project)
    else:
        print("Project creation failed!")