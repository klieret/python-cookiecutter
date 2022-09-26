# Python cookiecutter 🐍🍪✂️

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/klieret/python-cookiecutter/main.svg)](https://results.pre-commit.ci/latest/github/klieret/python-cookiecutter/main)
[![gitmoji](https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg)](https://gitmoji.dev)
[![License](https://img.shields.io/github/license/klieret/python-cookiecutter.svg)](https://github.com/klieret/python-cookiecutter/blob/main/LICENSE.txt)
[![PR welcome](https://img.shields.io/badge/PR-Welcome-%23FF8300.svg)](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project)

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for my
python projects using `setuptools`.

## ✨ Features

- Pre-commit hooks, including `codespell`, `mypy`, `black`, `flake8` and others
- Pre-configured logger in `util` subpackage
- Readme (including badges), license, changelog
- Link checker for all markdown files

## 🔥 Use it

```bash
cookiecutter git@github.com:klieret/python-cookiecutter.git
```

## 🔧 Development setup

```bash
pre-commit install
gitmoji -i
```
