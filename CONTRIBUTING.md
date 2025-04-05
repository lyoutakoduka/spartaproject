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
- User: leonidas

**Install WSL.**

```bat
wsl --install --distribution Ubuntu-24.04
```

**Login to Linux.**

```bat
wsl --distribution Ubuntu-24.04 --user leonidas
```

### 3-2: Apt

**Refresh the installable packages.**

```bash
sudo apt update
```

### 3-3: Docker

[Official Information](https://docs.docker.com/engine/install/)

_The conditions used for verification._

- Distribution: Ubuntu

#### 3-3-1: Packages

##### 3-3-1-1: Cleanup

**Remove old packages.**

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt remove $pkg; done
```

##### 3-3-1-2: Outside packages

**Install packages used for installation.**

```bash
sudo apt install ca-certificates curl
```

##### 3-3-1-3: Add repository

**Prepare downloading a public key.**

```bash
sudo install --mode 0755 --directory /etc/apt/keyrings
```

**Download the public key.**

```bash
sudo curl --fail --silent --show-error --location https://download.docker.com/linux/ubuntu/gpg --output /etc/apt/keyrings/docker.asc
```

**Change the permission of the public key.**

```bash
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

**Add the official Docker repository to Apt's package sources.**

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

**Refresh the installable packages again.**

```bash
sudo apt update
```

##### 3-3-1-4: Installation

**Install packages for Docker.**

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

#### 3-3-2: User

In order to execute Docker commands without "sudo".

[Official Information](https://docs.docker.com/engine/install/linux-postinstall/)

**Create the docker group.**

```bash
sudo groupadd docker
```

**Change the permission of the docker group.**

```bash
sudo usermod --append --groups docker $USER
```

**Log out.**

```bash
logout
```

**Login to Linux again.**

```bat
wsl --distribution Ubuntu-24.04 --user leonidas
```

#### 3-3-3: Devcontainer

[Official Information](https://code.visualstudio.com/docs/devcontainers/devcontainer-cli)

_The conditions used for verification._

- Package manager: npm

**Install the package manager for installing "Dev Container CLI".**

```bash
sudo apt install npm
```

**Install "Dev Container CLI".**

```bash
sudo npm install --global @devcontainers/cli
```

### 3-4: Git

**Install Git.**

```bash
sudo apt install git
```

### 3-5: IDE

_The conditions used for verification._

- IDE: VSCode
- OS: Windows

#### 3-5-1: Code editor

**Install VSCode**

[Official Information](https://code.visualstudio.com/download)

#### 3-5-2: VSCode Extensions

**Install VSCode WSL**

[Official Information](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)

**Install VSCode Dev Containers**

[Official Information](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## 4: Getting Started

### 4-1: Working Directory

_The conditions used for verification._

- Directory name: sparta_working

**Create the working directory.**

```bash
mkdir ~/sparta_working
```

**Move to the working directory.**

```bash
cd ~/sparta_working
```
