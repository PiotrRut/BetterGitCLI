"""
Main menu of the app with all the available options
"""

from PyInquirer import prompt, Separator
from sys import exit
from better_git_cli.repos import see_repos
from better_git_cli.user import change_user_details
from better_git_cli.sshkeys import manage_ssh_keys
from better_git_cli.languages import language_stats
from better_git_cli.new_repo import new_repo


# Main menu of the application
def start_menu():

    question = {
        "type": "list",
        "name": "main_menu",
        "message": "What would you like to do?",
        "choices": [
            {"name": "Manage existing repositories", "value": 1},
            {"name": "Create a new (remote) repository", "value": 2},
            {"name": "Manage my personal details", "value": 3},
            {"name": "View and delete my SSH keys", "value": 4},
            {"name": "Show my language stats", "value": 5},
            Separator(),
            {"name": "Exit to shell", "value": 6},
        ],
    }

    answers = prompt(question)

    if answers.get("main_menu") == 1:
        see_repos()

    if answers.get("main_menu") == 2:
        new_repo()

    if answers.get("main_menu") == 3:
        change_user_details()

    if answers.get("main_menu") == 4:
        manage_ssh_keys()

    if answers.get("main_menu") == 5:
        language_stats()

    if answers.get("main_menu") == 6:
        exit("Exiting now - see you later! 👋🏼")
