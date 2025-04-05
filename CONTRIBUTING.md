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
