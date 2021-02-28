"""
Main menu of the app with all the available options
"""

from PyInquirer import prompt, Separator
from sys import exit
from better_git_cli.repos import see_repos
from better_git_cli.user import change_user_details
from better_git_cli.sshkeys import manage_ssh_keys
from better_git_cli.languages import language_stats


# Main menu of the application
def start_menu():

    question = {
        "type": "list",
        "name": "main_menu",
        "message": "What would you like to do?",
        "choices": [
            {"name": "Manage my repositories", "value": 1},
            {"name": "Manage my personal details", "value": 2},
            {"name": "View and delete my SSH keys", "value": 3},
            {"name": "Show my language stats", "value": 4},
            Separator(),
            {"name": "Exit to shell", "value": 5},
        ],
    }

    answers = prompt(question)

    if answers.get("main_menu") == 1:
        see_repos()

    if answers.get("main_menu") == 2:
        change_user_details()

    if answers.get("main_menu") == 3:
        manage_ssh_keys()

    if answers.get("main_menu") == 4:
        language_stats()

    if answers.get("main_menu") == 5:
        exit("Exiting now - see you later! 👋🏼")
