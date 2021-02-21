# BetterGitCLI 

_Disclaimer: BetterGitCLI is not official GitHub software, nor is it in any way affiliated with GitHub_

BetterGitCli is a third party GitHub CLI client made with Python, providing extended and easier access to manage your 
GitHub account directly from your shell.

## Configuration

See below for instructions on how to configure BetterGitCLI before executing.

### GitHub access

In order to get access to your GitHub account you will need to authenticate with your GitHub access token. You can find instructions
on how to obtain it [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token). After generating
your token, export it as an env var in your shell:

```bash
$ export GITHUB_AUTH_TOKEN=<token>
```

:rotating_light: BetterGitCLI will never store your access token, and it will _only_ be stored locally on your machine.

### Dependencies

The following need to be installed on your machine in order to run this program:

- `PyInquirer` - [download](https://pypi.org/project/PyInquirer/) (pypi.org)
- `PyGithub` - [download](https://pypi.org/project/PyGithub/) (pypi.org)
- `colorama` - [download](https://pypi.org/project/colorama/) (pypi.org)

## Usage

```bash
$ python main.py
```

To navigate the UI, use your arrow keys (up and down) and select options
using `Enter`. You can also exit the program at any time by using the `^C` combination.

Via the UI, you can view all your repositories, manage branches and deployments, manage your
personal user details and much more!

## Contributing

All contributions to extend the functionality, fix any bugs (if you spot any) or make the code better or more effecient
are more than welcome - please feel free to open up a pull request!