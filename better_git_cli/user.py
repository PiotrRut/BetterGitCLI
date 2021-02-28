"""
All the functions and menus for managing user details and settings
"""

from PyInquirer import Separator, prompt
from better_git_cli.helpers import *
import better_git_cli.options as options


def change_user_details():

    git_user = github().get_user()

    list_options = [
        {
            "type": "list",
            "name": "user_mng",
            "message": f"{github().get_user().name}, what would you like to do?",
            "choices": [
                {"name": "Change my location", "value": 1},
                {"name": "Change my name", "value": 2},
                {"name": "Change my website URL", "value": 3},
                {"name": "Change my bio", "value": 4},
                Separator(),
                {"name": "Return to main menu", "value": 5},
                {"name": "Exit to shell", "value": 6},
            ],
        }
    ]

    answers = prompt(list_options)

    if answers.get("user_mng") == 1:
        print(f"Current location: {git_user.location}")
        new_location = input("Please provide a new location: ")
        if new_location:
            git_user.edit(location=new_location)
            success("Location changed successfully")
        else:
            error("ERROR: Location cannot be empty")

    elif answers.get("user_mng") == 2:
        new_name = input(
            f"{git_user.name}, please provide a new name for your profile: "
        )
        if new_name:
            git_user.edit(name=new_name)
            success("Name changed successfully")
        else:
            error("ERROR: Name cannot be empty")

    elif answers.get("user_mng") == 3:
        print(f"Current website URL: {git_user.blog}")
        new_url = input("Please provide a new URL: ")
        if new_url:
            git_user.edit(blog=new_url)
            success("Website URL changed successfully")
        else:
            error("ERROR: URL cannot be empty")

    elif answers.get("user_mng") == 4:
        print(f"Current bio: {git_user.bio}")
        new_bio = input("Please provide your new bio: ")
        if new_bio:
            git_user.edit(bio=new_bio)
            success("Bio updated successfully")
        else:
            error("ERROR: Bio cannot be empty")

    elif answers.get("user_mng") == 5:
        options.start_menu()

    elif answers.get("user_mng") == 6:
        exit("Exiting now - see you later! 👋🏼")

    change_user_details()
