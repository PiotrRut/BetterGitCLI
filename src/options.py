from PyInquirer import prompt, Separator
import os
from github import Github
from sys import exit
from colorama import Fore


def error(contents):
    print(Fore.RED + contents + Fore.RESET)


def success(contents):
    print(Fore.GREEN + contents + Fore.RESET)


# Authenticate and create a GitHub instance
def github():
    return Github(os.getenv('GITHUB_AUTH_TOKEN'))

# Main menu of the application
def start_menu():
    # OPTIONS #

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

    # FUNCTIONS #

    if answers.get('main_menu') == 1:
        see_repos()

    if answers.get('main_menu') == 2:
        change_user_details()

    if answers.get('main_menu') == 3:
        exit('Exiting now - see you later! 👋🏼')

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
        repos.extend((
            Separator(),
            {
                'name': 'Return to main menu',
                'value': 1
            },
            {
                'name': 'Exit to shell',
                'value': 2
            }

        ))
        return repos

    question = {
        'type': 'list',
        'name': 'repo',
        'message': 'Choose a repository',
        'choices': get_repos_as_options()
    }

    list_answer = prompt(question)

    if list_answer.get('repo') == 1:
        start_menu()

    elif list_answer.get('repo') == 2:
        exit('Exiting now - see you later! 👋🏼')

    repo = github().get_repo(list_answer.get('repo'))

    question2 = {
        'type': 'list',
        'name': 'repo_mng',
        'message': f'What would you like to do with {repo.name}',
        'choices': [
            {
                'name': 'Change name',
                'value': 1
            },
            {
                'name': 'Change description',
                'value': 2
            },
            {
                'name': 'Change URL',
                'value': 3
            },
            {
                'name': 'Change visibility',
                'value': 4
            },
            Separator(),
            {
                'name': 'Return to main menu',
                'value': 5
            },
            {
                'name': 'Exit to shell',
                'value': 6
            }
        ]
    }

    repo_answer = prompt(question2)

    if repo_answer.get('repo_mng') == 1:
        print(f'Current name: {repo.name}')
        new_name = input('Please provide a new name: ')
        if new_name:
            repo.edit(name=new_name)
            success('Name changed successfully')
        else:
            error('Error: Name cannot be empty')

    elif repo_answer.get('repo_mng') == 2:
        print(f'Current description: {repo.description}')
        new_description = input('Please provide a new description: ')
        if new_description:
            repo.edit(description=new_description)
            success('Description changed successfully')
        else:
            error('Error: Description cannot be empty')

    elif repo_answer.get('repo_mng') == 3:
        print(f'Current URL: {repo.homepage}')
        new_url = input('Please provide a new URL: ')
        if new_url:
            repo.edit(homepage=new_url)
            success('URL changed successfully')
        else:
            error('Error: URL cannot be empty')

    elif repo_answer.get('repo_mng') == 4:
        print(f'Current visibility: {"private" if repo.private else "public"}')
        question3 = {
            'type': 'list',
            'name': 'vis',
            'message': 'Choose visibility',
            'choices': [
                {
                    'name': 'Public',
                    'value': False
                },
                {
                    'name': 'Private',
                    'value': True
                }
            ]
        }
        vis_answer = prompt(question3)
        repo.edit(private=vis_answer.get('vis'))
        success('Visibility changed successfully')

    elif repo_answer.get('repo_mng') == 5:
        start_menu()

    elif repo_answer.get('repo_mng') == 6:
        exit('Exiting now - see you later! 👋🏼')

    see_repos()


def change_user_details():
    # OPTIONS #

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

    # FUNCTIONS #

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
