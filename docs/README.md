# Clara

[![GitHub Pages](https://img.shields.io/badge/%20-FFFFFF?style=social&logo=githubpages&logoColor=black&logoSize=auto)](https://fjrodafo.github.io/Clara/)
[![GitHub Stars](https://img.shields.io/github/stars/FJrodafo/Clara?style=social&logo=github&logoColor=black&label=Stars&labelColor=FFFFFF&color=FFFFFF)](https://github.com/FJrodafo/Clara/stargazers)

## Index

1. [Introduction](#introduction)
2. [Project structure](#project-structure)
3. [Clone the repository](#clone-the-repository)
4. [Install dependencies](#install-dependencies)
5. [Installation](#installation)
6. [Verify installation](#verify-installation)
7. [Usage](#usage)
8. [Uninstallation](#uninstallation)
9. [Example](#example)
10. [Resources](#resources)

## Introduction

Open-source AI assistant directly from the terminal!

This project has been developed on a [Linux](https://github.com/torvalds/linux) system. To learn more about the system, visit the [Dotfiles](https://github.com/FJrodafo/Dotfiles) repository.

## Project structure

```
/
├── docs/
|   ├── _config.yaml
|   ├── CODE_OF_CONDUCT.md
|   ├── README.md
|   └── SECURITY.md
├── CONTRIBUTING
├── LICENSE
├── .env
├── clara.md
└── Makefile
```

## Clone the repository

Open a terminal in the directory where you store your repositories and clone it with the following command:

```shell
# HTTPS
git clone https://github.com/FJrodafo/Clara.git
```

```shell
# SSH
git clone git@github.com:FJrodafo/Clara.git
```

## Install dependencies

Clara requires the following dependencies to be able to install/uninstall it via Makefile (In this case, they will be installed for a Linux Debian system via apt):

```shell
sudo apt update
sudo apt install -y build-essential coreutils
```

## Installation

Run the install target to set up Clara for your current user:

```shell
make install
```

This will:
- Copy the `clara` executable to `~/.local/bin/`
- Create the `~/.clara/logs/` directory for log files
- Prompt you for your Gemini API key if one isn't already configured, it will be saved to `~/.clara/.env`

Make sure `~/.local/bin` is in your `PATH`. If it isn't, add the following to your `~/.profile`:

```shell
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
```

Then reload your profile:

```shell
source ~/.profile
```

## Verify installation

After installing, confirm that Clara is accessible in your `PATH`:

```shell
command -v clara
```

If installed correctly, this should output:

```shell
~/.local/bin/clara
```

If nothing is returned, make sure `~/.local/bin` is in your `PATH`:

```shell
echo $PATH | tr ':' '\n' | nl
```

## Usage

Once installed, you can invoke Clara from anywhere:

```shell
clara
```

## Uninstallation

To remove Clara from your system:

```shell
make uninstall
```

This removes the `clara` executable from `~/.local/bin/`. Your configuration and logs in `~/.clara/` are preserved.

## Example

### Prompt

```md
💠 Clara - type 'exit' to quit.

> Hi, I'm FJrodafo, what's your name?
💠 Hello FJrodafo! It's nice to meet you. My name is Clara, and I'm an AI assistant created by you. How can I help you today?

> exit
💠 Clara - view logs at '~/.clara/logs/'
```

### Log

```md
# Clara 2026/03/31 22:27:36

> Hi, I'm FJrodafo, what's your name?

💠 Hello FJrodafo! It's nice to meet you. My name is Clara, and I'm an AI assistant created by you. How can I help you today?
```

## Resources

[Gemini API](https://ai.google.dev/gemini-api/docs#rest)
