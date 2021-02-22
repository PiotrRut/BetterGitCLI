from options import *
from helpers import *
from PyInquirer import prompt, Separator


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
