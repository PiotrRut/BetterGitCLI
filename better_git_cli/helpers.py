"""
Various helper functions used through out the application
"""

from github import Github
from colorama import Fore
import os


# Prints a green success message
def error(contents):
    print(Fore.RED + contents + Fore.RESET)


# Prints a red error message
def success(contents):
    print(Fore.GREEN + contents + Fore.RESET)


# Initialise and return a GitHub client instance
def github():
    return Github(os.getenv("GITHUB_AUTH_TOKEN"))
