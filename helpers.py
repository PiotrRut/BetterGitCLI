from PyInquirer import prompt, Separator
import os
from github import Github


# Authenticate and create a GitHub instance
def github():
    git = Github(os.getenv('GITHUB_AUTH_TOKEN'))
    return git


# Main menu of the application
def start_menu():

    # OPTIONS #

    question = {
        'type': 'list',
        'name': 'main_menu',
        'message': 'What would you like to do?',
        'choices': [
            {
                'name': 'See all repos',
                'value': 1
            },
            {
                'name': 'List deployments of a repository',
                'value': 2
            },
            {
                'name': 'Change my details',
                'value': 3
            },
            Separator(),
            {
                'name': 'Exit this application',
                'value': 4
            },
        ]
    }

    answers = prompt(question)

    # FUNCTIONS #

    if answers.get('main_menu') == 1:
        see_repos()

    if answers.get('main_menu') == 3:
        change_user_details()

    if answers.get('main_menu') == 4:
        exit('Exiting now - see you later!')

    return answers


def see_repos():
    # Fetch all users repos and return them as an array of options to pass to the selector menu
    def get_repos_as_options():
        repos = []
        for repo in github().get_user().get_repos():
            repos.append({
                'name': repo.name,
                'value': repo.id
            })
        return repos

    # OPTIONS #
    question = {
        'type': 'list',
        'name': 'repo',
        'message': 'Choose a repository',
        'choices': get_repos_as_options()
    }

    answers = prompt(question)

    # FUNCTIONS #

    for branch in github().get_repo(answers.get('repo')).get_branches():
        print(branch.name)


def change_user_details():

    # OPTIONS #

    options = [
        {
            'type': 'list',
            'name': 'user_mng',
            'message': 'What would you like to change?',
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
                    'name': 'Change my website url',
                    'value': 3
                },
                {
                    'name': 'Change my e-mail address',
                    'value': 4
                },
                Separator(),
                {
                    'name': 'Exit to main menu',
                    'value': 5
                },
                {
                    'name': 'Exit this application',
                    'value': 6
                }
            ]
        }
    ]

    answers = prompt(options)

    # FUNCTIONS #

    if answers.get('user_mng') == 1:
        github().get_user().edit(location=input('Please provide a new location: '))
        print('Location changed successfully')

    elif answers.get('user_mng') == 2:
        github().get_user().edit(name=input('Please provide a new name: '))
        print('Name changed successfully')

    elif answers.get('user_mng') == 3:
        github().get_user().edit(blog=input('Please provide a new URL: '))
        print('Website URL changed successfully')

    elif answers.get('user_mng') == 4:
        github().get_user().edit(email=input('Please provide a new e-mail address: '))
        print('E-mail address changed successfully')

    elif answers.get('user_mng') == 5:
        start_menu()

    elif answers.get('user_mng') == 6:
        exit('Exiting now - see you later 👋🏼')

    change_user_details()
