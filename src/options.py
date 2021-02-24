"""
Main menu of the app with all the available options
"""

from PyInquirer import prompt, Separator
from sys import exit
from repos import see_repos
from user import change_user_details


# Main menu of the application
def start_menu():

    question = {
        'type': 'list',
        'name': 'main_menu',
        'message': 'What would you like to do?',
        'choices': [
            {
                'name': 'Manage my repositories',
                'value': 1
            },
            {
                'name': 'Manage my personal details',
                'value': 2
            },
            Separator(),
            {
                'name': 'Exit to shell',
                'value': 3
            },
        ]
    }

    answers = prompt(question)

    if answers.get('main_menu') == 1:
        see_repos()

    if answers.get('main_menu') == 2:
        change_user_details()

    if answers.get('main_menu') == 3:
        exit('Exiting now - see you later! 👋🏼')
