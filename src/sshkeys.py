"""
All the functions and menus for managing and deleting user's SSH keys
"""

from PyInquirer import Separator, prompt
from helpers import *
import options


def manage_ssh_keys():

    git_user = github().get_user()

    list_options = [
        {
            'type': 'list',
            'name': 'ssh_keys',
            'message': f' {github().get_user().name}, what would you like to do?',
            'choices': [
                {
                    'name': 'View my SSH keys',
                    'value': 1
                },
                {
                    'name': 'Delete SSH keys',
                    'value': 2
                }
                ,
                Separator(),
                {
                    'name': 'Return to main menu',
                    'value': 3
                },
                {
                    'name': 'Exit to shell',
                    'value': 4
                }
            ]
        }
    ]

    answers = prompt(list_options)

    if answers.get('ssh_keys') == 1:
        if git_user.get_keys().totalCount == 0:
            print('Nothing to display.')
            manage_ssh_keys()
        else:
            for key in git_user.get_keys():
                print('Showing SSH keys...')
                print(f'KEY: {key.key} / ID: {key.id} / NAME: {key.title}')

    if answers.get('ssh_keys') == 2:
        if git_user.get_keys().totalCount == 0:
            print('You do not have any keys configured.')
            manage_ssh_keys()
        else:
            repos = []
            for key in git_user.get_keys():
                repos.append({
                    'name': f'KEY: {key.key} / ID: {key.id} / NAME: {key.title}',
                    'value': key.id
                })
            repos.extend((
                Separator(),
                {
                    'name': 'Return to main menu',
                    'value': 'exit_menu'
                },
                {
                    'name': 'Exit to shell',
                    'value': 'exit_shell'
                }

            ))

            question = {
                'type': 'list',
                'name': 'delete_key',
                'message': 'Choose a key to delete',
                'choices': repos
            }

            ssh_delete = prompt(question)

            warning = {
                'type': 'confirm',
                'message': f'Are you sure you want to delete key with ID {ssh_delete.get("delete_key")}?',
                'name': 'continue',
                'default': True,
            }

            warning_answer = prompt(warning)

            if warning_answer.get('continue') is True:
                git_user.get_key(ssh_delete.get('delete_key')).delete()
                success(f'Key with ID {key.id} successfully deleted.')
            else:
                manage_ssh_keys()

    elif answers.get('ssh_keys') == 3:
        options.start_menu()

    elif answers.get('ssh_keys') == 4:
        exit('Exiting now - see you later! 👋🏼')

    manage_ssh_keys()
