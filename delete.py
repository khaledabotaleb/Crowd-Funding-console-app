import json

from view_projects import view_projects


def delete_project(user_mail):
    view_projects(user_mail)
    project_name = input('\nSelect one project to delete : ')

    list = []
    json_file = open('projects_data.json')
    for line in json_file:
        Dict = json.loads(line)
        list.append(Dict)

    # search for project name and remove and update json file
    for dict in list:
        if dict['Title'] == project_name:
            list.remove(dict)
            # update in json file
            projects = open("projects_data.json", "w")
            for add_dict in list:
                json.dump(add_dict, projects)
                projects.write("\n")
            projects.close()

            print("\ndelete project successfully")
            break
    else:
        print("this project name is n't exist ,, please try again")
        delete_project(user_mail)