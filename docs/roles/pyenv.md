# Role pyenv
[back to index](../index.md#Roles)

## Summary
Pyenv is a Python version management tool, which lets you change the global Python version, install multiple versions and create directory specific versions (Python environments).

## Requires
* Debian-based system
* RHEL-based system

## Description
This role will install pyenv for each user individually. For both yum and apt based package managers, all dependencies (primarily needed for compiling python versions) are first downloaded. The installation is then done through the pyenv installer script which is run once when the user logs in.

## Variables

- `default_python_version`: String. The version of Python to be automatically installed for each in user at first login. This version is also set as the default version for that user (with `pyenv global`). Default: `system` (don't install a new version, but use the system's python version by default).

## See also

- [runeonce role](../roles/runonce.md)

## History
2022 Written by Sytse Groenwold (Utrecht University)

[back to index](../index.md#Roles)
