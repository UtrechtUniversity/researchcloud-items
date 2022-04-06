# Role poetry
[back to index](../index.md#Roles)

## Summary
Poetry is a Python package version management tool for easy packageing and dependency management.

## Requires
* Debian-based system.

## Description
This role will install poetry through the official documentation's [recommended installed](https://python-poetry.org/docs/master/#installing-with-the-official-installer).
The installtation is done on a per-user basis, as per the application's designed usage.
The python virtualenv dependency is first installed through Ansible's `apt` module.
This role was seperated from its playbook to facilitate reusability.

## Variables
None.

## See also

## History
2022 Written by Sytse Groenwold (Utrecht University)

[back to index](../index.md#Roles)
