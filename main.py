from PyInquirer import prompt, Separator
import os


def welcome():
    print('Welcome to BetterGitCLI! \nThis program requires your GitHub access token in order to work properly!'
          '\n(don`t worry - it will only be stored locally on your device!)')
    os.environ['TESTING'] = input('Please provide your token -> ')

    if len(os.environ.get('TESTING')) > 1:
        print('Thank you')
        print(os.environ.get('TESTING'))
    else:
        print('Something went wrong. Please try again')
        welcome()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    welcome()

