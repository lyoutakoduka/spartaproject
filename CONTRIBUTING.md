# How to setup development environment of spartaproject

## STEP1: Communication language

All documents must written as English. But, author [lyouta](https://github.com/lyoutakoduka) english isn't great. If you need perfect tech support, it was provided by Japanese :)

_Note: all documents are written on the premise that translation service like Google Translate._

## STEP2: Operating system (OS)

We basically develop on Windows now, but will support Linux including WSL very soon.

### Verified OS

- Windows 10: 64bit

## STEP3: Integrated development environment (IDE)

We basically develop on Visual Studio Code (VCCode).

### Verified IDE

- [VSCode](https://code.visualstudio.com/): latest version

### VSCode extension

Helpful extensions for development of spartaproject

**Edit source code**

- [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
- [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)
- [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
- [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)
- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)

**Advice source code**

- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
- [Flake8](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8)
- [Mypy Type Checker](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

**Test source code**

- [Python Test Explorer for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter)

**Server something for test**

- [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
- [SFTP](https://marketplace.visualstudio.com/items?itemName=Natizyskunk.sftp)
- [WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)

## STEP4: Programming language

We basically develop on Python.

### Verified version

- [Python-3.11.5](https://www.python.org/downloads/release/python-3115/): Recommend
- [Python-3.10.11](https://www.python.org/downloads/release/python-31011/)

### Outside dependent libraries

After installed Python, please install following dependent libraries by using pip (package manager).

- [paramiko](https://pypi.org/project/paramiko/)
- [pytest](https://pypi.org/project/pytest/)
- [python-dateutil](https://pypi.org/project/python-dateutil/)
- [pypiwin32](https://pypi.org/project/pypiwin32/)

### More dependent libraries

To develop spartaproject on VSCode, please install following dependent libraries by using pip.

- [black](https://pypi.org/project/black/)
- [flake8](https://pypi.org/project/flake8/)
- [flake8-docstrings](https://pypi.org/project/flake8-docstrings/)
- [isort](https://pypi.org/project/isort/)
- [mypy](https://pypi.org/project/mypy/)
- [pylance](https://pypi.org/project/pylance/)

## STEP5: Outside development tools

### Version control system (VCS)

We are using Git for VCS.

- [git](https://git-scm.com/)

### Run Linux commands on Windows

We use gow for the compatibility layer of Linux from Windows. But if it works, anything is fine.

- [gow](https://github.com/bmatzelle/gow)

## STEP6: Create spartaproject development directory

1. Create current working directory

`mkdir project`

2. Move current working directory

`cd project`

3. Clone repository from github

`git clone https://github.com/lyoutakoduka/spartaproject.git spartaproject`

4. Generated directory tree (Top three tiers)

```
project/
　　├ spartaproject/
　　　　├ context/
　　　　├ pyspartaproj/
　　　　├ script/
　　　　├ test/
```

## STEP7: Test spartaproject module

It is under construction... :)
