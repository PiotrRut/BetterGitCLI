"""
Language stats
"""

from PyInquirer import prompt
from better_git_cli.helpers import *
import better_git_cli.options as options


def language_stats():

    git_user = github().get_user()

    list_options = [
        {
            "type": "list",
            "name": "language_stats",
            "message": "",
            "choices": [
                {"name": "Return to main menu", "value": 1},
                {"name": "Exit to shell", "value": 2},
            ],
        }
    ]

    if git_user.get_repos().totalCount:
        repos_set = set()
        repos_list = []
        for repo in git_user.get_repos():
            if repo.language:
                repos_list.append(repo.language)
                repos_set.add(repo.language)

        print("-- YOUR LANGUAGE STATS --")
        for language in repos_set:
            print(f"{language}: {repos_list.count(language)} repo(s)")
    else:
        print("Your account does not have any repositories")

    answers = prompt(list_options)

    if answers.get("language_stats") == 1:
        options.start_menu()

    elif answers.get("language_stats") == 2:
        exit("Exiting now - see you later! 👋🏼")

    language_stats()
