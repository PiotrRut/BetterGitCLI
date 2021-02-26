![BannerImg](https://user-images.githubusercontent.com/43642399/108777456-bab79800-755b-11eb-8325-7904e0face0f.png)

<p align="center">
    <a href="https://github.com/PiotrRut/BetterGitCLI/actions/workflows/codeql-analysis.yml">
        <img src="https://github.com/PiotrRut/BetterGitCLI/actions/workflows/codeql-analysis.yml/badge.svg" />
    </a>
    <img src="https://travis-ci.com/PiotrRut/BetterGitCLI.svg?token=WYp4pRfPB9puZwpAYdtc&branch=master" />
    <img src="https://img.shields.io/pypi/pyversions/bettergitcli">
    <a href="https://pypi.org/project/bettergitcli/">
      <img src="https://img.shields.io/pypi/v/bettergitcli">
    </a>
</p>

> Disclaimer: BetterGitCLI is **not** official GitHub software, nor is it in any way affiliated with GitHub.

BetterGitCli is a third party GitHub CLI made with Python, providing easier access to managing your
GitHub account directly from your shell with simple and intuitive UI. It's based on `PyGithub` which is a wrapper library around the official GitHub REST API.

## Configuration

See below for instructions on how to configure BetterGitCLI. Note that Python 3.6 or higher is required to run this program.

### GitHub access

In order to gain access to your GitHub account you will need to authenticate with your GitHub access token. You can find instructions
on how to obtain it [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).

Your token must grant access to _"repo"_, _"user"_, _"delete_repo"_ and _"admin:public_key"_. After generating
your token, export it as an environmental variable in your shell 👇🏻

```bash
# bash / zsh
$ export GITHUB_AUTH_TOKEN=<token>

# powershell
$env:GITHUB_AUTH_TOKEN = "token"
```

🚨 BetterGitCLI will never store your access token, and it will *only be stored locally* on your machine.

### Installation
You can either install this program using `pip`, or clone it and run locally with Python. Click on one of the 
options down below to reveal the instructions 👇🏻

<details open>
  <summary><i><b>Install package with pip (preferred)</b></i></summary>
  
  This is the absolute easiest way to get started with BetterGitCLI! If you have `pip` installed, you can 
  download and install BetterGitCLI using this command:

  ```bash
  $ pip install bettergitcli
  ```

  After installation, you can run it from anywhere in your shell:
  
  ```bash
  $ bettergitcli
  ```
</details>

<details>
  <summary><i><b>Clone and run locally with Python</b></i></summary>

  If you prefer to clone this repository and run BetterGitCLI locally using your Python interpreter, you can
  do that as well. 
  
  Just remember that these dependencies need to be installed in order for this program
  to run:
  
  - `PyInquirer` - [download](https://pypi.org/project/PyInquirer/) (pypi.org)
  - `PyGithub` - [download](https://pypi.org/project/PyGithub/) (pypi.org)
  - `Colorama` - [download](https://pypi.org/project/colorama/) (pypi.org)
  
  This can be done easily using the provided `requirements.txt` file by running this in the project root:
  ```bash
  $ pip install -r requirements.txt
  ```
  
  After installation, run the program inside the `/better_git_cli` directory:

  ```bash
  $ python main.py
  ```
</details>


## Usage
To navigate the UI, use your arrow keys (up and down) and select options
using <kbd>Enter</kbd>. You can also exit the program at any time by using the <kbd>^C</kbd> (<kbd>Ctrl+C</kbd>) combination,
or by choosing the _"Exit to shell"_ option.

Via the UI, you can view all your repositories, manage branches and deployments, manage your
personal user details and much more! **Current functions include**:

- Repository management
    - View and edit repository details, such as the description, default branches, visibility and more!
    - Delete repositories
- User management
    - View and edit your personal details like your name, location or bio
- SSH keys management
    - View and delete SSH keys linked to your GitHub account
  

## Changelog
You can view the changelog [here](https://github.com/PiotrRut/BetterGitCLI/blob/master/CHANGELOG.md).

## Contributing
All contributions to add new features, fix any bugs (if you spot any) or make the code better or more efficient
are more than welcome - please feel free to raise an [issue](https://github.com/PiotrRut/BetterGitCLI/issues/new) or open up a pull request!
