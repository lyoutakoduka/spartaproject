# How to set up the development environment of our project.

## 1: Language

See "Language" and "Technical Support" section of [README.md](README.md)

## 2: Requirements

### 2-1: Operating system (OS)

Prepare the Linux environment.

### 2-2: Container

Prepare Docker and Devcontainer.

### 2-3: Version Control System (VCS)

Prepare Git.

### 2-4: Integrated Development Environment (IDE)

Prepare the Python friendly IDE.
And if you select VSCode, prepare the extensions "WSL" and "Dev Containers".

## 3: Installation

Let me explain with more specific examples.

### 3-1: WSL

[Official Information](https://learn.microsoft.com/en-us/windows/wsl/install)

_The conditions used for verification._

- OS: Windows
- Distribution: Ubuntu
- Distribution version: 24.04
- User: sparta

**Install WSL.**

```bat
wsl --install --distribution Ubuntu-24.04
```

**Login to Linux.**

```bat
wsl --distribution Ubuntu-24.04 --user sparta
```

### 3-2: Apt

**Refresh the installable packages.**

```bash
sudo apt update
```
