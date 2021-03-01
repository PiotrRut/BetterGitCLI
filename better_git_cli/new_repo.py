"""
Create a new repository
"""

from PyInquirer import prompt
from better_git_cli.helpers import *
import better_git_cli.options as options
import webbrowser
from github import GithubException
from prompt_toolkit.validation import Validator, ValidationError
import regex


class RepoNameValidate(Validator):
    def validate(self, document):
        ok = regex.match("^[A-Za-z0-9_.-]*$", document.text)
        if not ok:
            raise ValidationError(
                message="Name can not contain spaces",
                cursor_position=len(document.text),
            )  # Move cursor to end


def new_repo():
    git_user = github().get_user()

    are_you_sure = {
        "type": "confirm",
        "name": "are_you_sure",
        "message": "Are you sure you want to create a new repository?",
        "default": False,
    }

    questions = [
        {
            "type": "input",
            "name": "repo_name",
            "message": "Please provide a name:",
            "validate": RepoNameValidate,
        },
        {
            "type": "input",
            "name": "repo_desc",
            "message": "Please provide a description (ENTER to leave blank):",
        },
        {
            "type": "confirm",
            "name": "repo_private",
            "message": "Do you want this repo to be private?",
            "default": True,
        },
    ]
    are_you_sure_check = prompt(are_you_sure)
    if not are_you_sure_check.get("are_you_sure"):
        options.start_menu()
    else:
        answers = prompt(questions)
        try:
            git_user.create_repo(
                name=answers.get("repo_name"),
                description=answers.get("repo_desc"),
                private=answers.get("repo_private"),
            )
        except GithubException:
            error("Something went wrong! Please try again")
            options.start_menu()
        else:
            success(
                f'Repo created at -> https://github.com/{git_user.login}/{answers.get("repo_name")}'
            )
            webbrowser.open(
                f'https://github.com/{git_user.login}/{answers.get("repo_name")}'
            )
            options.start_menu()
