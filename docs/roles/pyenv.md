# Role pyenv
[back to index](../index.md#Roles)

## Summary
Pyenv is a Python version management tool, which lets you change the global Python version, install multiple versions and create directory specific versions (Python environments).

## Requires
* Debian-based system
* RHEL-based system

## Description
This role will install pyenv for each user individually. For both yum and apt based package managers, all dependencies (primarily needed for compiling python versions) are first downloaded. The installation is then done through the pyenv installer script which is run once when the user logs in.

The role supports installing the latest version of python available in the OS's package manager and registering that python version with `pyenv`. This is useful because OS distributions generally ship with older python versions by default, and when installing an addtional specific python version (e.g. `apt install python3.12` ), `pyenv` will not know about it by default. See the special `system-latest` value for the `default_python_version` variable below. **Note**: this is only supported on Ubuntu at the moment.

## Variables

- `default_python_version`: String. The version of Python to be automatically installed for each in user at first login. This version is also set as the default version for that user (with `pyenv global`). Default: `system` (don't install a new version, but use the system's python version by default). Possible values:

    * `3.11` (installs latest `3.11` python, e.g. `3.11.1`)
    * `3.8.4.1` (install specific version).
    * Special value: `system-latest`. Will use the OS's package manager (e.g. `apt`) to fetch the latest packaged python version, and this version will be used as `pyenv`'s global python version instead of the older, default system python version.

## See also

- [runeonce role](../roles/runonce.md)

## History
2022-2024 Written by Sytse Groenwold and Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
