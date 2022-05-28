import json


def view_projects(user_mail):
    print("-------------- User Projects ----------------")
    list = []
    json_file = open('projects_data.json')
    for line in json_file:
        Dict = json.loads(line)
        if Dict['User'] == user_mail:
            list.append(Dict)

            if len(list) == 0:
                from login import login_menu
                print("no project for you ")
                login_menu()
            else:
                print("-------------- User Projects ----------------")
                counter = 1
                for dict in list:
                    print("Project: %d" % counter)
                    print("Project Title: %s" % dict["Title"])
                    print("Project Description: %s" % dict["Details"])
                    print("Total Target: %s" % dict["Total_Target"])
                    print("Start Date: %s" % dict["Start_Time"])
                    print("End Date: %s" % dict["End_Time"])
                    print("____________________________________________________________")
                    counter +=1