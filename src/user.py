from options import *
from helpers import *
from PyInquirer import Separator, prompt


def change_user_details():

    git_user = github().get_user()

    options = [
        {
            'type': 'list',
            'name': 'user_mng',
            'message': f' {github().get_user().name}, what would you like to do?',
            'choices': [
                {
                    'name': 'Change my location',
                    'value': 1
                },
                {
                    'name': 'Change my name',
                    'value': 2
                },
                {
                    'name': 'Change my website URL',
                    'value': 3
                },
                Separator(),
                {
                    'name': 'Return to main menu',
                    'value': 4
                },
                {
                    'name': 'Exit to shell',
                    'value': 5
                }
            ]
        }
    ]

    answers = prompt(options)

    if answers.get('user_mng') == 1:
        print(f'Current location: {git_user.location}')
        new_location = input('Please provide a new location: ')
        if new_location:
            git_user.edit(location=new_location)
            success('Location changed successfully')
        else:
            error('Error: location cannot be empty')

    elif answers.get('user_mng') == 2:
        print(f'Current name: {git_user.name}')
        new_name = input('Please provide a new name: ')
        if new_name:
            git_user.edit(name=new_name)
            success('Name changed successfully')
        else:
            error('Error: name cannot be empty')

    elif answers.get('user_mng') == 3:
        print(f'Current website URL: {git_user.blog}')
        new_url = input('Please provide a new URL: ')
        if new_url:
            git_user.edit(blog=new_url)
            success('Website URL changed successfully')
        else:
            error('Error: URL cannot be empty')

    elif answers.get('user_mng') == 4:
        start_menu()

    elif answers.get('user_mng') == 5:
        exit('Exiting now - see you later! 👋🏼')

    change_user_details()
