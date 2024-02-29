# Playbook python_workbench
[back to index](../index.md#Playbooks)

## Summary
Installs a Python development environment equiped with 
*[pyenv](https://pypi.org/project/pyenv/)* 
to allow the user to select an arbitrary Python version and
*[poetry](https://pypi.org/project/poetry/)* 
to facilitate Python module dependency management.

## Requires
Linux operating system

## Description
The Linux distribution influences which Python3 and pip3 versions are installed system-wide. This component therefore installs `pyenv` and `poetry` via the `runonce` role, so that each user on the system can manage their own Python environment. `pyenv` and `poetry` are installed (in userspace) the first time the user logs in.

## Variables

- `default_python_version`: String. This version of Python to be automatically installed for each in user via `pyenv`, at first login. This version is also set as the default version for that user (with `pyenv global`). If this parameter is set to an empty string, no version of Python will be installed automatically. Default: `3.9.18`.

## See also

- role [runonce](../roles/runonce.md)

## History
2021 Written by Ton Smeele (Utrecht University)

[back to index](../index.md#Playbooks)
