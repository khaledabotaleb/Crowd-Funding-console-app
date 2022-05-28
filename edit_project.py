import json

from create_project import validate_datetime


def edit_project(user_mail):
    print("--------------- Edit Project --------------------")
    project_title = input("Project Title: ")

    list = []
    json_file = open('projects_data.json')
    for line in json_file:
        Dict = json.loads(line)
        list.append(Dict)

        # search for poject name
    update_items = []
    for dict in list:
        if dict['Title'] == project_title and dict['User'] == user_mail:
            project = {"Title": input("New Project Title: "),
                       "Details": input("New Project Details: "),
                       "Total_Target": input("New Total Target: "),
                       "Start_Time": validate_datetime(input("New Start Time (dd/mm/yy): ")),
                       "End_Time": validate_datetime(input("New End Time (dd/mm/yy): ")),
                       "User": user_mail
                       }
            dict['Title'] = project['Title'],
            dict['Details'] = project["Details"]
            dict['Total_Target'] = project["Total_Target"]
            dict['Start_Time'] = project["Start_Time"]
            dict['End_Time'] = project["End_Time"]
            dict['User'] = project["User"]
            print(dict)
            # update in json file
            projects = open("projects_data.json", "w")
            json.dump(dict, projects)
            projects.write("\n")
            projects.close()

        else:
            print("this project name is n't exist ,, please try again")
            edit_project(user_mail)

    print("\nupdate project successfully")


