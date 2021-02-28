"""
All the functions and menus for managing user repositories
"""

from PyInquirer import prompt, Separator
from better_git_cli.helpers import *
import better_git_cli.options as options


def see_repos():

    # Fetch all users repos and return them as an array of options to pass to the selector menu
    def get_repos_as_options():
        repos = []
        if github().get_user().get_repos().totalCount >= 1:
            for repo in github().get_user().get_repos():
                repos.append({"name": repo.name, "value": repo.id})
            repos.extend(
                (
                    Separator(),
                    {"name": "Return to main menu", "value": 1},
                    {"name": "Exit to shell", "value": 2},
                )
            )
        return repos

    # CHOOSE A REPOSITORY TO MANAGE

    question = {
        "type": "list",
        "name": "repo",
        "message": "Choose a repository",
        "choices": get_repos_as_options(),
    }

    if len(get_repos_as_options()):
        repo_list_answer = prompt(question)
    else:
        print("No repositories to display")

    if repo_list_answer.get("repo") == 1:
        options.start_menu()

    elif repo_list_answer.get("repo") == 2:
        exit("Exiting now - see you later! 👋🏼")

    repo = github().get_repo(repo_list_answer.get("repo"))

    # WHAT TO DO WITH CHOSE REPO
    # (at this point the user have chosen one from list)

    question2 = {
        "type": "list",
        "name": "repo_mng",
        "message": f"What would you like to do with {repo.name}",
        "choices": [
            {"name": "Change name", "value": 1},
            {"name": "Change description", "value": 2},
            {"name": "Change URL", "value": 3},
            {"name": "Change visibility", "value": 4},
            {"name": "Change default branch", "value": 5},
            {"name": "Delete this repository", "value": 6},
            Separator(),
            {"name": "Return to main menu", "value": 7},
            {"name": "Exit to shell", "value": 8},
        ],
    }

    repo_answer = prompt(question2)

    if repo_answer.get("repo_mng") == 1:
        new_name = input(f"Please provide a new name for {repo.name}: ")
        if new_name:
            repo.edit(name=new_name)
            success("Name changed successfully")
        else:
            error("ERROR: Name cannot be empty")

    elif repo_answer.get("repo_mng") == 2:
        print(f"Current description: {repo.description}")
        new_description = input("Please provide a new description: ")
        if new_description:
            repo.edit(description=new_description)
            success("Description changed successfully")
        else:
            error("ERROR: Description cannot be empty")

    elif repo_answer.get("repo_mng") == 3:
        print(f"Current URL: {repo.homepage}")
        new_url = input("Please provide a new URL: ")
        if new_url:
            repo.edit(homepage=new_url)
            success("URL changed successfully")
        else:
            error("ERROR: URL cannot be empty")

    elif repo_answer.get("repo_mng") == 4:
        print(f'Current visibility: {"Private" if repo.private else "Public"}')
        question3 = {
            "type": "list",
            "name": "vis",
            "message": "Choose visibility",
            "choices": [
                {"name": "Public", "value": False},
                {"name": "Private", "value": True},
            ],
        }
        vis_answer = prompt(question3)
        repo.edit(private=vis_answer.get("vis"))
        success("Visibility changed successfully")

    elif repo_answer.get("repo_mng") == 5:
        print(f"Current default branch: {repo.default_branch}")
        print(f"Available branches: {[i.name for i in repo.get_branches()]}")
        new_branch = input("Please provide the new default branch: ")
        if new_branch:
            repo.edit(default_branch=new_branch)
            success("Default branch changed successfully")
        else:
            error("ERROR: Branch name cannot be empty")

    elif repo_answer.get("repo_mng") == 6:
        warning = {
            "type": "confirm",
            "message": f"Are you sure you want to delete {repo.name}? This is irreversible!",
            "name": "continue",
            "default": True,
        }
        delete_answer = prompt(warning)
        if delete_answer.get("continue") is True:
            github().get_repo(repo.id).delete()
            success(f"{repo.name} successfully deleted!")

    # Back to menu
    elif repo_answer.get("repo_mng") == 7:
        options.start_menu()

    # Exit the app
    elif repo_answer.get("repo_mng") == 8:
        exit("Exiting now - see you later! 👋🏼")

    see_repos()
