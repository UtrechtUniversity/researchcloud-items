# Role system_python
[back to index](../index.md#Roles)

## Summary
Installs latests version of python available through the system package manager and sets the fact `python_system_python_path` to the path to the newly installed python interpreter, so it can be used in other roles or playbooks.

## Requires

* Ubuntu 20.04 or higher (other systems can be supported, but work is needed to define latest versions).

## Description
This role will check the `python_system_python_latest_versions` default variable for a value for the latest available Python version on the OS (e.g.: `3.9` on Ubuntu 20.04) and use the system's package manager to install:

- the relevant version of python
- the relevant version of the python-venv package
- a corresponding version of pip

## History
2024 Written by Dawa Ometto (Utrecht University)

[back to index](../index.md#Roles)
