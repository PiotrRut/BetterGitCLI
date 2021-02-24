![BannerImg](https://user-images.githubusercontent.com/43642399/108777456-bab79800-755b-11eb-8325-7904e0face0f.png)

<p align="center">
    <a href="https://github.com/PiotrRut/BetterGitCLI/actions/workflows/codeql-analysis.yml">
        <img src="https://github.com/PiotrRut/BetterGitCLI/actions/workflows/codeql-analysis.yml/badge.svg" />
    </a>
</p>

> Disclaimer: BetterGitCLI is **not** official GitHub software, nor is it in any way affiliated with GitHub.

BetterGitCli is a third party GitHub CLI made with Python, providing easier access to managing your
GitHub account directly from your shell with simple and intuitive UI. It's based on `PyGithub` which is a wrapper library around the official GitHub REST API.

## Configuration

See below for instructions on how to configure BetterGitCLI.

### GitHub access

In order to gain access to your GitHub account you will need to authenticate with your GitHub access token. You can find instructions
on how to obtain it [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).

Your token must grant access to _"repo"_, _"user"_, _"delete_repo"_ and _"admin:public_key"_. After generating
your token, export it as an environmental variable in your shell :point_down:

```bash
# It is important that the name is the same
$ export GITHUB_AUTH_TOKEN=<token>
```

:rotating_light: BetterGitCLI will never store your access token, and it will *only* be stored locally on your machine.

### Dependencies

The following need to be installed on your machine in addition to Python 3 in order to run this program:

- `PyInquirer` - [download](https://pypi.org/project/PyInquirer/) (pypi.org)
- `PyGithub` - [download](https://pypi.org/project/PyGithub/) (pypi.org)
- `Colorama` - [download](https://pypi.org/project/colorama/) (pypi.org)

This can be done easily using the provided `requirements.txt` file by running this in the project root :point_down:
```bash
$ python -m pip install -r requirements.txt
```

## Usage

Run the application inside the `/src` directory :point_down:

```bash
$ python main.py
```

---

To navigate the UI, use your arrow keys (up and down) and select options
using <kbd>Enter</kbd>. You can also exit the program at any time by using the <kbd>^C</kbd> (<kbd>Ctrl+C</kbd>) combination,
or by choosing the _"Exit to shell"_ option.

Via the UI, you can view all your repositories, manage branches and deployments, manage your
personal user details and much more! **Current functions include**:

- Repository management
    - View and edit repository details, such as the description, default branches, visibility and more!
    - Delete repositories
- User management
    - View and edit your personal details like your name, location and website URL
- SSH keys management
    - View and delete SSH keys linked to your GitHub account

## Contributing

All contributions to add new features, fix any bugs (if you spot any) or make the code better or more efficient
are more than welcome - please feel free to raise an [issue](https://github.com/PiotrRut/BetterGitCLI/issues/new) to open up a pull request!
