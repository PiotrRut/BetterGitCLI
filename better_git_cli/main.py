from options import start_menu
from helpers import github
from colorama import init, Fore
import os
from sys import exit


def cli_main():
    g = github()
    if 'GITHUB_AUTH_TOKEN' in os.environ:
        print(f'Welcome to BetterGitCLI, {g.get_user().name}!')
    else:
        exit(Fore.RED + 'ERROR: Could not find your GitHub token. \nPlease export it first in your shell as "GITHUB_AUTH_TOKEN".' + Fore.RESET)

    sm = start_menu()


if __name__ == '__main__':
    # Init colorama (needed for Windows)
    init()
    cli_main()

